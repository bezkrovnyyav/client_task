"""
Module APIClient include API requests functionality.

Module JSONPlaceholderClient provide an interface for working with the JSONPlaceholder API.

Module LocalDataStorage is used for storing data locally.
"""

from api_client import APIClient
from client import JSONPlaceholderClient
from local_storage import LocalDataStorage

if __name__ == '__main__':
    # Creating an instance of the APIClient
    fake_api_key = 'custome_fake_api_key'  # Replace with your fake API key
    api_client = APIClient(base_url='https://jsonplaceholder.typicode.com', api_key=fake_api_key)

    # Creating instances of JSONPlaceholderClient and LocalDataStorage
    json_client = JSONPlaceholderClient(api_client=api_client)
    local_storage = LocalDataStorage()

    # Receiving posts and comments
    json_client.get_posts()
    json_client.get_comments()

    # Saving values locally
    local_storage.save_data('sample_data', {'example_key': 'example_value'})

    # Displaying the results of posts and comments
    print('Post: ', json_client.api_response.get('posts')[0], '\n')
    print('Comment: ', json_client.api_response.get('comments')[0])
