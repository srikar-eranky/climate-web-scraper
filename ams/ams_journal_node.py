from bs4 import BeautifulSoup
import requests
from ams_base_node import AmsBaseNode
from ams.ams_volume_node import AmsVolumeNode
from custom_driver import get_page_content

class AmsJournalNode(AmsBaseNode):
    def __init__(self, name, url, base_url, parent):
        super().__init__(name, url, base_url, parent)
        self.pd_column = 'Journal'

    def expand_node(self):
        # fill in code for expanding a journal
        # create a volume node for every volume in the journal
        # for the number of volumes, create a volume node for each volume - will include the volume number
        try:
            response = get_page_content(self.url)
            print(response)
            soup = BeautifulSoup(response.content, 'html.parser')
            target_items = soup.find_all('li', class_='ajax-node-opener type-volume text-title c-Link-emphasize color-text my-2 py-3 border-bottom-dark shut')
            if target_items:
                print(len(target_items))
                self.children = []
                for item in target_items:
                    try:
                        target_div = item.find('div',class_='label')
                        text = target_div.text
                        vol_num = text[7:text.index('(')-1]
                        vol_year = text[text.index('(')+1:text.index(')')]
                        vol_name = "Volume " + vol_num
                        print("Extracting from " + vol_name + "(" + vol_year + ")")
                        child = AmsVolumeNode(name=vol_name,base_url=self.base_url,parent=self,vol_number=vol_num)
                        self.children.append(child)
                        child.expand_node()
                    except:
                        print("couldn't find div")
            else:
                print("cannot find")
        except Exception as error:
            print("something went wrong", error)

