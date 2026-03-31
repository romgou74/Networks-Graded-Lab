import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G1 = nx.Graph()
with open('Part I/Graph1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        G1.add_edge(row[0], row[1])

print(G1)

G2 = nx.Graph()
with open('Part I/Graph2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        G2.add_edge(row[0], row[1])

print(G2)


def plot_degree_dist(G):
    degree_hist = nx.degree_histogram(G) 
    degree_hist = np.array(degree_hist, dtype=float)
    degree_prob = degree_hist/G.number_of_nodes()
    plt.loglog(np.arange(degree_prob.shape[0]),degree_prob,'b.')
    plt.xlabel('k')
    plt.ylabel('p(k)')
    plt.title('Degree Distribution')
    plt.show()

plot_degree_dist(G1)
plot_degree_dist(G2)

# Average degree of an undirected graph k = 2*number of edges/number of nodes
def average_deg(graph):
    k = 2 * float(len(graph.edges)) / float(len(graph.nodes))
    print(k)

average_deg(G1)
average_deg(G2)

def max_degrees(G):
    degrees = [val for (node, val) in G.degree()]
    nodes = [node for (node, val) in G.degree()]
    maximum = max(degrees)
    return (nodes[degrees.index(maximum)], maximum)

print(max_degrees(G1))
print(max_degrees(G2))