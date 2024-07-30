#!/usr/bin/env python3
"""Integration tests for GithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload, "expected_repos": expected_repos, "apache2_repos": apache2_repos},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class-level patches"""
        cls.get_patcher = patch('requests.get', side_effect=cls.mocked_requests_get)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level patches"""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """Mocked requests.get"""
        if url == 'https://api.github.com/orgs/google':
            return MockResponse(org_payload)
        elif url == 'https://api.github.com/orgs/google/repos':
            return MockResponse(repos_payload)
        return None

    def test_public_repos(self):
        """Test public_repos method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)

class MockResponse:
    """Mock response class"""
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data

if __name__ == "__main__":
    unittest.main()
