"""
Typing module is used to support type annotations in code.

Module APIClient is a base class for making API requests..
"""
from typing import Any, Dict

from api_client import APIClient


class JSONPlaceholderClient(object):
    """
    Provides a Singleton instance for interacting with the JSONPlaceholder API and managing resulting data locally.

    This class ensures only a single instance exists, allowing access to the API via its methods.
    """

    _instance = None

    def __new__(cls, api_client: APIClient) -> 'JSONPlaceholderClient':
        """Create and returns a Singleton instance of JSONPlaceholderClient if one doesn't already exist.

        Args:
            api_client (APIClient): An instance of the APIClient to be used for API interactions.

        Returns:
            JSONPlaceholderClient: The Singleton instance of the JSONPlaceholderClient.
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.api_client = api_client
            cls._instance.api_response: Dict[str, Any] = {}
        return cls._instance

    def get_posts(self) -> None:
        """Get post data with JSONPlaceholder API."""
        self.api_response['posts'] = self.api_client.make_request('posts')

    def get_comments(self) -> None:
        """Send a request to the API to get comment data."""
        self.api_response['comments'] = self.api_client.make_request('comments')
