#!/usr/bin/env python3
"""A module for testing the client module.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock, PropertyMock
from typing import Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(
        self,
        org: str,
        expected_response: Dict,
        mock_get_json: MagicMock
    ) -> None:
        """Tests the `org` method."""
        mock_get_json.return_value = MagicMock(return_value=expected_response)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), expected_response)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )

    def test_public_repos_url(self):
        """Test the _public_repos_url property """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_json):
        """ Text more public repos """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ unit-test for GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """integration tests for the GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """ Before each method"""
        conf = {'return_value.json.side_effect':
                [
                    cls.org_payload, cls.repos_payload,
                    cls.org_payload, cls.repos_payload
                ]
                }
        cls.get_patcher = patch('requests.get', **conf)
        cls.mock = cls.get_patcher.start()
