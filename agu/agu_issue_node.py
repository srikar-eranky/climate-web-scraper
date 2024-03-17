from base_nav_node import BaseNavNode
from custom_driver import get_page_content
from bs4 import BeautifulSoup
import time

class AGUIssueNode(BaseNavNode):
    def __init__(self, name, url, base_url):
        super().__init__(name, url, base_url)
        self.pd_column = 'Issue'
    
    def convert_link_for_download(self, link):
        link = link.replace('epdf', 'pdfdirect')
        link += '?download=true'
        return link
    
    def expand_node(self):
        try:
            page_content = get_page_content(self.url)
            soup = BeautifulSoup(page_content, 'html.parser')
            article_elements = soup.find_all('div', class_='issue-items-container bulkDownloadWrapper')

            self.children = []
            for element in article_elements:
                divs = [a.parent for a in element.find_all('a', class_='issue-item__title visitable')]
                for div in divs:
                    try:
                        title = div.find('h2').text
                        access_div = div.find('div', class_='pull-left').find('div', class_='open-access access-type')
                        pdf_link = div.find('a', string='PDF')
                        if title != 'Issue Information' and access_div is not None:
                            self.children.append(BaseNavNode(title, self.convert_link_for_download(pdf_link['href']), self.base_url))
                    except:
                        print("Error in " + self.name + '. Ignoring...')
            if len(self.children) == 0:
                raise Exception('No Articles were found for this issue - ' + self.url)
        except Exception as e:
            time.sleep(1)
            self.expand_node()