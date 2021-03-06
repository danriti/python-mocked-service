# -*- coding: utf-8 -*-

"""
Tests for the Github API library.

"""

import unittest

from httmock import with_httmock

import github
import mocks.github


class TestGithub(unittest.TestCase):

    @with_httmock(mocks.github.resource_get)
    def test_get_repository(self):
        owner = 'appneta'
        repo = 'burndown'

        results = github.get_repository(owner, repo)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('name' in results)
        self.assertEqual(results['name'], repo)

    @with_httmock(mocks.github.resource_get)
    def test_get_user(self):
        user = 'danriti'

        results = github.get_user(user)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('login' in results)
        self.assertEqual(results['login'], user)

if __name__ == '__main__':
    unittest.main()
