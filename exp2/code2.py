import networkx as nx
# import csv
import matplotlib.pyplot as plt

g = nx.barabasi_albert_graph(n=70, m=2)
nx.draw_networkx(g, with_labels=True)
plt.show()
