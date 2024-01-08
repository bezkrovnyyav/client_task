"""
Module requests is used for get date from url.

Typing module is used to support type annotations in code.
"""
from typing import Dict

import requests


class APIClient(object):
    """Base class for making API requests."""

    def __init__(self, base_url: str) -> None:
        """
        Initialize APIClient with base_url param.

        Args:
            base_url(str): variable include url address for request
        """
        self.base_url = base_url

    def make_request(self, endpoint: str) -> Dict:
        """
        Make a generic API request to JSONPlaceholder site.

        Args:
            endpoint(str): The API endpoint to make the request to.

        Returns:
            Dict: JSON response from the API endpoint.
        """
        response = requests.get(f'{self.base_url}/{endpoint}', timeout=3)
        http_success_code = 200

        if response.status_code == http_success_code:
            return response.json()
        print(f'Failed to fetch data from {endpoint}')
        return {}
