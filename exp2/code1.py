import networkx as nx
import csv
import matplotlib.pyplot as plt

g = nx.erdos_renyi_graph(n=50, p=0.1)
nx.draw_networkx(g, with_labels=True)
plt.show()
