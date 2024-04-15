"""Connect to webpage for data collect
"""
import io
from os import link
import requests
from bs4 import BeautifulSoup as bs

class HttpData:
    """Basic class to manage data
    """
    def  __init__(self) -> None:
        self.url = 'localhost'
        self.all_links = []

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
        
    def save_results_in_file(self, filename: str, datatobesaved, savemode: str, islist: bool = False):
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
            with open(filename, savemode) as file:
                if islist == True:
                    for item in datatobesaved:
                        file.write("%s\n" % item)
                else:
                    file.write(datatobesaved)
        except IOError as err:
            print(err)

    def analyse_downloaded_content(self, downloadedpagecontent):
        
        content = bs(downloadedpagecontent.content, 'html.parser')
        return content
    
    def find_all(self, content: bs, xpath):
        value = content.find_all('a', class_=xpath)
        return value

HttpDataObject = HttpData()
pagecontent = HttpDataObject.connect_to_web_page_and_return_data('https://justjoin.it')
#HttpDataObject.save_results_in_file("RawData.txt", pagecontent.content, "wb")
pagecontentformatted = HttpDataObject.analyse_downloaded_content(pagecontent)
HttpDataObject.save_results_in_file("AnalysedData.txt", pagecontentformatted.prettify().encode('utf-8'), "wb")

for x in HttpDataObject.find_all(pagecontentformatted, 'offer_list_offer_link css-4lqp8g'):
    HttpDataObject.all_links.append(str(x))

for counter in range(0, len(HttpDataObject.all_links), 1):
    HttpDataObject.all_links[counter] = str(HttpDataObject.all_links[counter]).removeprefix('<a class="offer_list_offer_link css-4lqp8g" href="')
    HttpDataObject.all_links[counter] = str(HttpDataObject.all_links[counter].removesuffix('"></a>'))
    HttpDataObject.all_links[counter] = 'https://justjoin.it' + HttpDataObject.all_links[counter]

HttpDataObject.save_results_in_file("Links.txt", HttpDataObject.all_links, "w", True)

print(type(HttpDataObject.all_links))