"""Typing module is used to support type annotations in code."""
from typing import Any, Dict


class LocalDataStorage(object):
    """Class for storing data locally."""

    def __init__(self) -> None:
        """Initialize LocalDataStorage with data param."""
        self.response_data: Dict[str, Any] = {}

    def save_data(self, key: str, data_to_save: Any) -> None:
        """
        Save data with a given key.

        Args:
            key (str): The key under which the data will be saved.
            data_to_save (Any): Data to be saved.
        """
        self.response_data[key] = data_to_save

    def get_data(self, key: str) -> Any:
        """
        Retrieve data with a given key.

        Args:
            key (str): The key associated with the data.

        Returns:
            Any: The data corresponding to the provided key, if found. Otherwise, None.
        """
        return self.response_data.get(key)
