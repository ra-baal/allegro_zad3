#!/usr/bin/python3

import flask
import requests


app = flask.Flask(__name__)


def github_request(username: str) -> list:
    """
    Sends the request to GitHub.
    :param username: The name of a GitHub user.
    :return: JSON data as a Python list.
    """

    url = f"https://api.github.com/users/{username}/repos"
    headers = {'accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)

    json_list = response.json()  # list

    return json_list


def prepare_repos_list(json_list: list) -> str:
    """
    Extracts the necessary data (names and stars of repos).
    :param json_list: JSON data (list) to extract the necessary data.
    :return: JSON data (str).
    """

    repos_stars = []
    for repo in json_list:
        name = repo['name']
        stars = repo['stargazers_count']
        repos_stars.append({"name": name,
                            "stars": stars})

    json_data = flask.json.dumps(repos_stars)

    return json_data


def prepare_stars_sum(json_list: list) -> str:
    """
    Extracts the necessary data (sum of stars in repos).
    :param json_list: JSON data (list).
    :return: JSON data (str).
    """

    starssum = sum(repo["stargazers_count"] for repo in json_list)

    json_data = flask.json.dumps({"starssum": starssum})

    return json_data


@app.route('/<username>/starssum')
def stars_sum(username):
    """
    Endpoint. The sum of the stars for the user.
    """
    github_response = github_request(username)

    try:
        json_data = prepare_stars_sum(github_response)
    except TypeError:
        json_data = flask.json.dumps({"message": "Such user does not exist."})

    response = flask.Response(json_data, mimetype='application/json')

    return response


@app.route('/<username>')
def repos_list(username):
    """
    Endpoint. The list of repository names and number of stars.
    """
    github_response = github_request(username)

    try:
        json_data = prepare_repos_list(github_response)
    except TypeError:
        json_data = flask.json.dumps({"message": "Such user does not exist."})

    response = flask.Response(json_data, mimetype='application/json')
    return response


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

    app.run(debug=True)
    # app.run(debug=False)


#
