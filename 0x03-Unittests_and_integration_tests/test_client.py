#!/usr/bin/env python3
"""A module for testing the client module.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
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
