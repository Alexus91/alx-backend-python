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

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property."""
        mock_org_p = {'repos_url': "https://api.github.com/users/google/repos"}
        with patch.object(
                GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mock_org_p
            client = GithubOrgClient("google")
            public_repos_url = client._public_repos_url
            self.assertEqual(public_repos_url, mock_org_p['repos_url'])
