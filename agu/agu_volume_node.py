from base_nav_node import BaseNavNode
from agu.agu_issue_node import AGUIssueNode
from custom_driver import get_page_content
from bs4 import BeautifulSoup
from tqdm import tqdm
import time

class AGUVolumeNode(BaseNavNode):
    def __init__(self, name, url, base_url):
        super().__init__(name, url, base_url)
        self.pd_column = 'Volume'
    
    def expand_node(self):
        try:
            page_content = get_page_content(self.url)
            soup = BeautifulSoup(page_content, 'html.parser')
            parent_element = soup.find('h2', string='Issues').parent
            links = parent_element.find_all('a')
            
            self.children = []
            for link in tqdm(links):
                text = link.text.strip()
                if text[:6] == 'Volume':
                    child_node = AGUIssueNode(text[-7:], self.base_url + link['href'], self.base_url)
                    self.children.append(child_node)
                    child_node.expand_node()
        except:
            time.sleep(1)
            self.expand_node()