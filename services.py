import requests
import json

def github_request(username: str) -> list:
    """
    Sends the request to GitHub.
    :param username: The name of a GitHub user.
    :return: JSON data as a Python list.
    """

    url = f"https://api.github.com/users/{username}/repos"
    headers = {'accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)

    return response.json()  # list


def prepare_repos_list(json_list: list) -> str:
    """
    Extracts the necessary data (names and stars of repos).
    :param json_list: JSON data (list) to extract the necessary data.
    :return: JSON data (str).
    """

    repos_stars = list(map(
        lambda repo: {
            'name': repo['name'],
            'stars': repo['stargazers_count']
        }, json_list))

    return json.dumps(repos_stars)


def prepare_stars_sum(json_list: list) -> str:
    """
    Extracts the necessary data (sum of stars in repos).
    :param json_list: JSON data (list).
    :return: JSON data (str).
    """

    starssum = sum(repo["stargazers_count"] for repo in json_list)

    return json.dumps({"starssum": starssum})


#
