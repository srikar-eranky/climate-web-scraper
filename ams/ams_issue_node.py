from base_nav_node import BaseNavNode
import re
from custom_driver import get_page_content

class AmsIssueNode(BaseNavNode):
    def __init__(self, name, url, base_url):
        super().__init__(name, url, base_url)
        self.pd_column = "Issue"

    def expand_node(self):
        self.children = []
        # get page content from each issue
        try:
            page_contents = get_page_content(self.url)
            page_contents = page_contents.strip()
            page_contents = page_contents[page_contents.find("ARTICLES"):]
            label_index = page_contents.find("<div class=\"label\">")
            if label_index != -1:
                page_contents = page_contents[:label_index]
            pattern = r'<a target="_self" href="([^"]*)" class="c-Button--link">([^<]*)</a>'
            occurrences = re.findall(pattern,page_contents)
            for href, text in occurrences:
                url = "https://journals.ametsoc.org" + href
                title = text.strip()
                child_node = BaseNavNode(name=title, url=url, base_url=self.base_url)
                self.children.append(child_node)
        except:
            print("An error occurred")