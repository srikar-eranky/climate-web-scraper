from base_nav_node import BaseNavNode
from custom_driver import get_page_content
from bs4 import BeautifulSoup
import time

class EUCIssueNode(BaseNavNode):
    def __init__(self, name, url):
        super().__init__(name, url)
        self.pd_column = 'Issue'
    
    def convert_to_pdf_link(self, url):
        splits = url.split('/')
        journal = splits[2].split('.')[0]
        suffix = '-' + splits[-4] + '-' + splits[-3] + '-' + splits[-2] + '.pdf'
        return url + journal + suffix
    
    def expand_node(self):
        try:
            page_content = get_page_content(self.url)
            soup = BeautifulSoup(page_content, 'html.parser')
            article_elements = soup.find_all('a', class_='article-title')

            self.children = []
            for element in article_elements:
                child_node = BaseNavNode(element.text, self.convert_to_pdf_link(element['href']))
                self.children.append(child_node)
                child_node.expand_node()

            if len(self.children) == 0:
                raise Exception('No Articles were found for this issue - ' + self.url)
        except Exception as e:
            time.sleep(1)
            self.expand_node()