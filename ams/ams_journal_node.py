from base_nav_node import BaseNavNode
from ams.ams_volume_node import AmsVolumeNode
from custom_driver import get_page_content

class AmsJournalNode(BaseNavNode):
    def __init__(self, name, url, base_url):
        super().__init__(name, url, base_url)
        self.pd_column = 'Journal'

    def expand_node(self):
        self.children = []
        # fill in code for expanding a journal
        # create a volume node for every volume in the journal
        # for the number of volumes, create a volume node for each volume - will include the volume number
        try:
            num_volumes = 0
            if(self.name == "aies"):
                num_volumes = 3
            elif(self.name == "bams"):
                num_volumes = 105
            elif(self.name == "clim"):
                num_volumes = 37
            elif(self.name == "atsc"):
                num_volumes = 81
            i = num_volumes
            if(num_volumes == 3):
                stop_point = 1
            else:
                stop_point = num_volumes-4
            while(i >= stop_point):
                vol_name = "Volume " + str(i)
                print("Extracting from " + vol_name)
                child = AmsVolumeNode(name=vol_name,base_url=self.base_url,vol_number=i, journal=self.name)
                self.children.append(child)
                i -= 1
                child.expand_node()
        except Exception as error:
            print("something went wrong", error)