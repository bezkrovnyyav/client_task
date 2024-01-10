"""
Module requests is used for get date from url.

Typing module is used to support type annotations in code.
"""
from typing import Dict

import requests


class APIClient(object):
    """Base class for making API requests."""

    def __init__(self, base_url: str, api_key: str) -> None:
        """
        Initialize APIClient with base_url and API key.

        Args:
            base_url(str): variable include url address for request
            api_key(str): API key for accessing the API
        """
        self.base_url = base_url
        self.api_key = api_key  # Add API key parameter

    def make_request(self, endpoint: str) -> Dict:
        """
        Make a generic API request to JSONPlaceholder site.

        Args:
            endpoint(str): The API endpoint to make the request to.

        Returns:
            Dict: JSON response from the API endpoint.
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}  # Use API key in request headers
        response = requests.get(
            f'{self.base_url}/{endpoint}',
            headers=headers,
            timeout=3,
        )
        http_success_code = 200

        if response.status_code == http_success_code:
            return response.json()
        print(f'Failed to fetch data from {endpoint}')
        return {}
