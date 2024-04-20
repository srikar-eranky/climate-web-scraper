from base_nav_node import BaseNavNode
from ams.ams_issue_node import AmsIssueNode
from custom_driver import get_page_content

class AmsVolumeNode(BaseNavNode):
    def __init__(self, name, base_url, vol_number, journal):
        super().__init__(name, base_url)
        self.vol_number = vol_number
        self.journal = journal
        self.pd_column = "Volume"

    def expand_node(self):
        self.children = []
        # create an issue node for every issue in the volume
        issue_num = 1
        while True:
            error_string = "Sorry, we could not find the page that you are looking for."
            link = "https://journals.ametsoc.org/view/journals/" + self.journal + "/" + str(self.vol_number) + "/" + str(issue_num) + "/" + self.journal + "." + str(self.vol_number) + ".issue-" + str(issue_num) + ".xml"
            page_content = get_page_content(link)
            if(error_string in page_content):
                uri = "https://journals.ametsoc.org/view/journals/" + self.journal + "/" + str(self.vol_number) + "/" + str(issue_num) + "-" + str(issue_num+1) + "/" + self.journal + "." + str(self.vol_number) + ".issue-" + str(issue_num) + "-" + str(issue_num+1) + ".xml"
                if(error_string not in get_page_content(uri)):
                    new_name = "Issue " + str(issue_num) + "-" + str(issue_num+1)
                    child = AmsIssueNode(name=new_name,url=uri,base_url=self.base_url)
                    issue_num += 2
                    self.children.append(child)
                    child.expand_node()
                    continue
                break
            issue_name = "Issue " + str(issue_num)
            print("Extracting from " + issue_name)
            child = AmsIssueNode(name=issue_name,url=link,base_url=self.base_url)
            self.children.append(child)
            child.expand_node()
            issue_num += 1