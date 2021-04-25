#!/usr/bin/python3

import flask
import services


app = flask.Flask(__name__)


@app.route('/<username>/starssum')
def stars_sum(username):
    """
    Endpoint. The sum of the stars for the user.
    """
    github_response = services.github_request(username)

    try:
        json_data = services.prepare_stars_sum(github_response)
    except TypeError:
        json_data = flask.json.dumps({"message": "Such user does not exist."})

    return flask.Response(json_data, mimetype='application/json')


@app.route('/<username>')
def repos_list(username):
    """
    Endpoint. The list of repository names and number of stars.
    """
    github_response = services.github_request(username)

    try:
        json_data = services.prepare_repos_list(github_response)
    except TypeError:
        json_data = flask.json.dumps({"message": "Such user does not exist."})

    return flask.Response(json_data, mimetype='application/json')


@app.errorhandler(404)
def error404(e):
    """
    Resource not found.
    """

    json_data = flask.jsonify(error=str(e))
    return json_data, 404


@app.route('/', methods=['GET'])
def form():
    """
    Form page.
    """

    return flask.render_template('form.html', title="GitHub users' repositories")


@app.route('/', methods=['POST'])
def form_redirection():
    """
    Form page redirection.
    """

    username = flask.request.form.get('username')
    list_or_sum = flask.request.form.get('list-or-sum')

    if list_or_sum == 'list':
        return flask.redirect(f'/{username}')
    else:
        return flask.redirect(f'/{username}/starssum')


if __name__ == '__main__':

    # app.run(debug=True)
    app.run(debug=False)


#
