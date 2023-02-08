import networkx as nx
import csv
import matplotlib.pyplot as plt

g = nx.karate_club_graph()
# g = nx.Graph()
# with open("dolphins.csv", mode='r')as file:
#     csvFile = csv.DictReader(file)
#     for line in csvFile:
#         g.add_edge(int(line['Source'])-1, int(line['Target'])-1)

# g = nx.Graph()
# with open("football.csv", mode='r')as file:
#     csvFile = csv.DictReader(file)
#     for line in csvFile:
#         g.add_edge(int(line['Source'])-1, int(line['Target'])-1)

degree_centrality = nx.degree_centrality(g)
closeness_centrality = nx.closeness_centrality(g)
betweenness_centrality = nx.betweenness_centrality(g)


print("Degree centrality: \n", degree_centrality)
print("------------------------")
print("Betweenness centrality: \n", betweenness_centrality)
print("------------------------")
print("Closeness centrality: \n", closeness_centrality)


dc_sizes = [50 + v * 1000 for v in degree_centrality.values()]
plt.subplot(3, 1, 1)
plt.title("Degree centrality")
nx.draw_networkx(g, with_labels=True, node_size=dc_sizes,
                 font_size=8, node_color='#FF0000')

bc_sizes = [50 + v * 1000 for v in betweenness_centrality.values()]
plt.subplot(3, 1, 2)
plt.title("Betweeness centrality")
nx.draw_networkx(g, with_labels=True, node_size=bc_sizes,
                 font_size=8, node_color='#0000FF')

cc_sizes = [50 + v * 1000 for v in closeness_centrality.values()]
plt.subplot(3, 1, 3)
plt.title("Closeness centrality")
nx.draw_networkx(g, with_labels=True, node_size=cc_sizes,
                 font_size=8, node_color='#FFFF00')
plt.show()
