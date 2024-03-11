"""Connect to webpage for data collect
"""
import requests

class HttpData:
    """Basic class to manage data
    """
    def  __init__(self) -> None:
        self.url = 'localhost'

    def connect_to_web_page_and_return_data(self, url: str):
        """Connect to web page and collect data

        Args:
            url (str): Webpage address

        Returns:
            Any: Read element from webpage
        """
        try:
            self.url = url
            return requests.get(self.url, timeout = 10).status_code
        except requests.HTTPError as err:
            return err

HttpDataObject = HttpData()
print(HttpDataObject.connect_to_web_page_and_return_data('https://justjoin.it/'))