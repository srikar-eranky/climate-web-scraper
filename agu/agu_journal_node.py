from base_nav_node import BaseNavNode
from agu.agu_volume_node import AGUVolumeNode
from custom_driver import get_page_content
from bs4 import BeautifulSoup
import time

class AGUJournalNode(BaseNavNode):
    def __init__(self, name, url, base_url):
        super().__init__(name, url, base_url)
        self.pd_column = 'Journal'
    
    def expand_node(self):
        try:
            page_content = get_page_content(self.url)
            soup = BeautifulSoup(page_content, 'html.parser')
            parent_element = soup.find('ul', class_='rlist loi__list').parent
            links = parent_element.find_all('a')

            self.children = []
            for link in links:
                text = link.text.strip()
                if text[7:13] == 'Volume' and int(text[:4]) >= 2020:
                    volume_name = text[7:]
                    print('Extracting from ' + volume_name)
                    child = AGUVolumeNode(volume_name, self.base_url + link['href'], self.base_url)
                    self.children.append(child)
                    child.expand_node()
        except:
            time.sleep(1)
            self.expand_node()