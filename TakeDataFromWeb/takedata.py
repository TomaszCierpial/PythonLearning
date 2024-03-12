"""Connect to webpage for data collect
"""
import io
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
            return requests.get(self.url, timeout = 10)
        except requests.HTTPError as err:
            print(err)
            return err
    def save_results_in_file(self, filename: str, datatobesaved, savemode: str):
        """Save collected data to file

        Args:
            filename (str): Result file name
            datatobesaved (str): Data to be saved
            savemode (str): Opening mode
            The argument mode points to a string beginning with one of the following
            sequences (Additional characters may follow these sequences.):

            ``r''   Open text file for reading.  The stream is positioned at the
                    beginning of the file.

            ``r+''  Open for reading and writing.  The stream is positioned at the
                    beginning of the file.

            ``w''   Truncate file to zero length or create text file for writing.
                    The stream is positioned at the beginning of the file.

            ``w+''  Open for reading and writing.  The file is created if it does not
                    exist, otherwise it is truncated.  The stream is positioned at
                    the beginning of the file.

            ``a''   Open for writing.  The file is created if it does not exist.  The
                    stream is positioned at the end of the file.  Subsequent writes
                    to the file will always end up at the then current end of file,
                    irrespective of any intervening fseek(3) or similar.

            ``a+''  Open for reading and writing.  The file is created if it does not
                    exist.  The stream is positioned at the end of the file.  Subse-
                    quent writes to the file will always end up at the then current
                    end of file, irrespective of any intervening fseek(3) or similar.
            
            ``wb''  Truncate file to zero length or create text file for writing.
                    The stream is positioned at the beginning of the file.
        """
        try:
            with io.open(filename, savemode) as file:
                file.write(datatobesaved)
        except IOError as err:
            print(err)

HttpDataObject = HttpData()
pagecontent = HttpDataObject.connect_to_web_page_and_return_data('https://justjoin.it/')
HttpDataObject.save_results_in_file("Results.txt", pagecontent.content, "wb")
