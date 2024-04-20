from ams.ams_node import AmsNode
node = AmsNode('AMS')
node.expand_node()
df = node.to_pandas()
df.to_csv('ams_links.csv')
