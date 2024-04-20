from base_nav_node import BaseNavNode
from ams.ams_journal_node import AmsJournalNode

class AmsNode(BaseNavNode):
    def __init__(self, name):
        super().__init__(name)
        self.pd_column = 'Website'
        self.base_url = 'https://journals.ametsoc.org/'
    
    def expand_node(self):
        journal_links = [
            ('bams', 'https://journals.ametsoc.org/view/journals/bams/bams-overview.xml'),
            ('aies', 'https://journals.ametsoc.org/view/journals/aies/aies-overview.xml'),
            ('clim', 'https://journals.ametsoc.org/view/journals/clim/clim-overview.xml'), #journal of climate
            ('atsc', 'https://journals.ametsoc.org/view/journals/atsc/atsc-overview.xml?contents=all-volumes') #journal of atmospheric sciences
        ]

        self.children = []

        for journal, link in journal_links:
            print("Navigating into journal - " + journal)
            url = link + "?contents=latest-issue"
            child = AmsJournalNode(name=journal, url=url, base_url=self.base_url)
            self.children.append(child)
            child.expand_node()
            

