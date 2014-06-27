# -*- coding: utf-8 -*-

"""
github

This module contains methods for accessing the Github API v3.

https://developer.github.com/v3/

"""

import requests


GITHUB_AUTHORITY = 'api.github.com'


def get_repository(owner, repo):
    """ Get respository information.

    :param owner: The name of the repository owner.
    :param repo: The name of the repository.
    :rtype: dict

    """
    uri = 'https://{0}/repos/{1}/{2}'.format(GITHUB_AUTHORITY, owner, repo)
    response = requests.get(uri)
    response.raise_for_status()
    return response.json()


def get_user(user):
    """ Get user information.

    :param user: The name of the GitHub user.
    :rtype: dict

    """
    uri = 'https://{0}/users/{1}'.format(GITHUB_AUTHORITY, user)
    response = requests.get(uri)
    response.raise_for_status()
    return response.json()
