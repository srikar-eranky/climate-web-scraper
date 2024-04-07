from ams_base_node import AmsBaseNode
from bs4 import BeautifulSoup
import requests
import time

class AmsIssueNode(AmsBaseNode):
    def __init__(self, name, url, base_url, parent):
        super().__init__(name, url, base_url, parent)
        self.pd_column = "Issue"

    def expand_node(self):
        self.children = []
        # get page content from each issue
        try:

            response = requests.get(self.url)
            soup = BeautifulSoup(response.content, 'html.parser')
            target_divs = soup.find_all('div',class_='display-flex flex-col flex-6 color-black flex-nowrap pt-2 pr-2 pb-2 pl-2')
            for div in target_divs:
                try:
                    title = div.find('h1',class_='typography-body text-display4 font-ui fw-3     color-primary f-4 ln-3').text
                    link = div.find('a',class_='c-Button--link')
                    child = AmsBaseNode(name=title,url=link['href'],base_url=self.base_url)
                    self.children.append(child)
                    child.expand_node()
                except:
                    print("There was an error")
        except:
            time.sleep(1)
            self.expand_node()

        
