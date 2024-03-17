from base_nav_node import BaseNavNode
from euc.euc_journal_node import EUCJournalNode

class EUCNode(BaseNavNode):
    def __init__(self, name):
        super().__init__(name)
        self.pd_column = 'Website'
    
    def expand_node(self):
        journal_list = [
            ('Atmospheric Chemistry and Physics', 'https://acp.copernicus.org/articles'),
            ('Earth System Dynamics', 'https://esd.copernicus.org/articles/'),
            ('Earth System Science Data', 'https://essd.copernicus.org/articles/'),
            ('Geoscientific Model Development', 'https://gmd.copernicus.org/articles/'),
            ('Ocean Science', 'https://os.copernicus.org/articles/')
        ]

        self.children = []
        for journal, link in journal_list:
            print("Navigating into journal - " + journal)
            child_node = EUCJournalNode(journal, link)
            self.children.append(child_node)
            child_node.expand_node()