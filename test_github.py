# -*- coding: utf-8 -*-

"""
Tests for the Github API library.

"""

import unittest

import github


class TestGithub(unittest.TestCase):

    def test_get_repository(self):
        owner = 'appneta'
        repo = 'burndown'

        results = github.get_repository(owner, repo)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('name' in results)
        self.assertEqual(results['name'], repo)


if __name__ == '__main__':
    unittest.main()
