from base_nav_node import BaseNavNode
from agu.agu_journal_node import AGUJournalNode

class AGUNode(BaseNavNode):
    def __init__(self, name):
        super().__init__(name)
        self.pd_column = 'Website'
        self.base_url = 'https://agupubs.onlinelibrary.wiley.com'
    
    def expand_node(self):
        journal_list = [
            ('AGU Advances', 'https://agupubs.onlinelibrary.wiley.com/loi/2576604x'),
            ('Geophysical Research Letters', 'https://agupubs.onlinelibrary.wiley.com/loi/19448007'),
            ('JGR Atmospheres', 'https://agupubs.onlinelibrary.wiley.com/loi/21698996'),
            ('Reviews of Geophysics', 'https://agupubs.onlinelibrary.wiley.com/loi/19449208')
        ]

        self.children = []
        for journal, link in journal_list:
            print("Navigating into journal - " + journal)
            child_node = AGUJournalNode(journal, link, self.base_url)
            self.children.append(child_node)
            child_node.expand_node()