#!/usr/bin/python3

# from flask import Flask
# from flask import render_template
# from flask import request, redirect, url_for, flash
import flask
import requests


# todo: class ServerApplication


app = flask.Flask(__name__)

def github_request(username: str):
    """
    Sends the request to GitHub.
    :param username: The name of a GitHub user.
    :return: todo: What returned? json (list of dicts?)
    """

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)

    content = response.content
    json_list = response.json()  # list
    raw = response.raw
    text = response.text

    return json_list


def prepare_repos_list(json_list):

    repos_stars = []
    for repo in json_list:
        name = repo['name']
        stars = repo['stargazers_count']
        repos_stars.append({name: stars})

    repos_stars = flask.json.dumps(repos_stars)

    return repos_stars  # todo: i tak zamieniam to potem na str? jest sens używania modułu json? (json to jest string!)


def prepare_stars_sum(json_list):

    starssum = sum(repo["stargazers_count"] for repo in json_list)

    json_data = flask.json.dumps({"starssum": starssum})

    return json_data


@app.route('/<username>/starssum')
def stars_sum(username):

    github_response = github_request(username)

    try:
        json_data = prepare_stars_sum(github_response)
    except TypeError:
        json_data = flask.json.dumps({"message": "Such user does not exist."})

    response = flask.Response(json_data, mimetype='application/json')

    return response


@app.route('/<username>')
def repos_list(username):

    github_response = github_request(username)

    try:
        json_data = prepare_repos_list(github_response)
    except TypeError:
        json_data = flask.json.dumps({"message": "Such user does not exist."})

    response = flask.Response(json_data, mimetype='application/json')
    return response


@app.errorhandler(404)
def resource_not_found(e):

    json_data = flask.jsonify(error=str(e))
    return json_data, 404


@app.route('/', methods=['GET', 'POST'])
def index():

    if flask.request.method == 'POST':

        formdata = flask.request.form.items()
        username = next(formdata)[1]

        return flask.redirect(f'/{username}')

    return '''<form method="POST"> <input name="username" type="text">
    <input type="submit">
    </form>
    '''


if __name__ == '__main__':

    app.run(debug=True)


#
