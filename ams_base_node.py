import pandas as pd

class AmsBaseNode:
    def __init__(self, name, url=None, base_url=None):
        self.name = name
        self.url = url
        self.base_url = base_url
        self.children = None
        self.pd_column = None
    
    def expand_node(self):
        pass

    def display_nav_tree(self, tabs=''):
        if self.children is None:
            print(tabs + self.name + ' - ' + self.url)
        else:
            print(tabs + self.name)
            for child in self.children:
                child.display_nav_tree(tabs + '\t')
    
    def to_pandas(self):
        if self.children is None or len(self.children) == 0:
            return pd.DataFrame({'Title': [self.name], 'PDF Link': [self.url]})
        else:
            df_list = []
            for child in self.children:
                df_list.append(child.to_pandas())
            df = pd.concat(df_list)
            df.insert(loc=0, column=self.pd_column, value=[self.name]*len(df))
            return df