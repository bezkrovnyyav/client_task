"""
Typing module is used to support type annotations in code.

Module APIClient is a base class for making API requests..
"""
from typing import Any, Dict, List, Union

from api_client import APIClient


class JSONPlaceholderClient(object):
    """Provides an interface for working with the JSONPlaceholder API and saving the resulting data locally."""

    def __init__(self, api_client: APIClient) -> None:
        """
        Initialize JSONPlaceholderClient with api_client parameter.

        Args:
            api_client(APIClient): an instance of the APIClient.
        """
        self.api_client = api_client
        self.api_response: Dict[str, Any] = {}

    def get_posts(self) -> None:
        """Get post data with JSONPlaceholder API."""
        self.api_response['posts'] = self.api_client.make_request('posts')

    def get_comments(self) -> None:
        """Send a request to the API to get a list of comments."""
        self.api_response['comments'] = self.api_client.make_request('comments')

    def save_data_locally(self, key: str, response_data: Union[List, Dict]) -> None:
        """
        Save response data locally using a provided key.

        Args:
            key (str): The key to save the response data.
            response_data (Union[List, Dict]): Data to be saved, can be a list or a dictionary.
        """
        self.api_response[key] = response_data
