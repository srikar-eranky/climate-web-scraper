from ams_base_node import AmsBaseNode
from ams.ams_issue_node import AmsIssueNode
import requests

class AmsVolumeNode(AmsBaseNode):
    def __init__(self, name, base_url,parent,vol_number):
        super().__init__(name, base_url,parent)
        self.vol_number = vol_number
        self.pd_column = "Volume"

    def expand_node(self):
        self.children = []
        # create an issue node for every issue in the volume
        while True:
            issue_num = 1
            try:
                journal_name = self.parent.name
                link = "https://journals.ametsoc.org/view/journals/" + journal_name + "/" + self.vol_number + "/" + issue_num + "/" + journal_name + "." + self.vol_number + ".issue-" + issue_num + ".xml"
                response = requests.get(link)
            except:
                print("There was an issue")
                break
            issue_name = "Issue " + issue_num
            print("Extracting from " + issue_name)
            child = AmsIssueNode(name=issue_name,url=link,base_url=self.base_url,parent=self)
            self.children.append(child)
            issue_num += 1
            child.expand_node()