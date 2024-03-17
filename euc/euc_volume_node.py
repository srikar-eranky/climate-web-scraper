from base_nav_node import BaseNavNode
from euc.euc_issue_node import EUCIssueNode
from tqdm import tqdm
import time

class EUCVolumeNode(BaseNavNode):
    def __init__(self, name, soup_element):
        super().__init__(name)
        self.soup_element = soup_element
        self.pd_column = 'Volume'
    
    def expand_node(self):
        try:
            elements = self.soup_element.findAll('span', class_='triangle')[1:]
            self.children = []
            for element in tqdm(elements):
                link = element.find('a')
                if link.text[:5] == 'Issue':
                    child_node = EUCIssueNode(link.text, link['href'])
                    self.children.append(child_node)
                    child_node.expand_node()
        except Exception as e:
            time.sleep(1)
            self.expand_node()