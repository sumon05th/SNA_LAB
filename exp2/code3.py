from networkx.generators.community import LFR_benchmark_graph
import networkx as nx
import matplotlib.pyplot as plt
n = 250
tau1 = 3
tau2 = 1.5
mu = 0.1
g = LFR_benchmark_graph(
    n, tau1, tau2, mu, average_degree=5, min_community=20, seed=10
)
nx.draw_networkx(g, with_labels=True)
plt.show()