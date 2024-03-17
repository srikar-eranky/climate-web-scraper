from base_nav_node import BaseNavNode
from euc.euc_volume_node import EUCVolumeNode
from custom_driver import get_page_content
from bs4 import BeautifulSoup
import time

class EUCJournalNode(BaseNavNode):
    def __init__(self, name, url):
        super().__init__(name, url)
        self.pd_column = 'Journal'
    
    def expand_node(self):
        try:
            page_content = get_page_content(self.url)
            soup = BeautifulSoup(page_content, 'html.parser')
            elements = soup.find_all('a', class_='show-hide')

            self.children = []
            for element in elements:
                volume_text = element.parent.text.split(',')[0].strip()
                date_text = element.parent.text.split(',')[1][:5]
                if volume_text[:6] == 'Volume' and int(date_text) >= 2020:
                    print('Extracting from ' + volume_text)
                    child = EUCVolumeNode(volume_text, element.parent.parent)
                    self.children.append(child)
                    child.expand_node()
        except:
            time.sleep(1)
            self.expand_node()