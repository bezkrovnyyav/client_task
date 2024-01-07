"""
Module requests is used for get date from url.

Typing module is used to support type annotations in code.
"""
from typing import Any, Dict, List, Union

import requests


class JSONPlaceholderClient(object):
    """Provides an interface for working with the JSONPlaceholder API and saving the resulting data locally."""

    base_url: str = 'https://jsonplaceholder.typicode.com'

    def __init__(self) -> None:
        """
        Initialize JSONPlaceholderClient with api_response param.

        :param api_response: dictionary to store the API response
        :type api_response: Dict
        """
        self.api_response: Dict[str, Any] = {}

    def get_posts(self) -> None:
        """Get post data with JSONPlaceholder API."""
        response = requests.get(f'{self.base_url}/posts', timeout=3)
        http_success_code = 200
        if response.status_code == http_success_code:
            self.api_response['posts'] = response.json()
        else:
            print('Failed to fetch posts')

    def get_comments(self) -> None:
        """Send a request to the API to get a list of posts."""
        response = requests.get(f'{self.base_url}/comments', timeout=3)
        http_success_code = 200
        if response.status_code == http_success_code:
            self.api_response['comments'] = response.json()
        else:
            print('Failed to fetch comments')

    def save_data_locally(self, key: str, response_data: Union[List, Dict]) -> None:
        """
        Save response data locally using a provided key.

        Args:
            key (str): The key to identify the response data.
            response_data (Union[List, Dict]): The data retrieved from the API response.
        """
        self.api_response[key] = response_data


if __name__ == '__main__':
    # Creating a JSONPlaceholderClient Instance
    client: JSONPlaceholderClient = JSONPlaceholderClient()

    # Receiving posts and comments
    client.get_posts()
    client.get_comments()

    # Saving values locally
    sample_data: Dict[str, str] = {'example_key': 'example_value'}
    client.save_data_locally('sample_data', sample_data)

    # Displaying the results of posts and comments
    print('Post: ', client.api_response.get('posts')[0], '\n')

    print('Comment: ', client.api_response.get('comments')[0])
