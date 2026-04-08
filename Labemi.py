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

# Source - https://stackoverflow.com/q/53958700
# Posted by Amit Mek, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-31, License - CC BY-SA 4.0

def plot_degree_dist(G, title='Degree Distribution', log_scale=False):
    degree_hist = nx.degree_histogram(G)
    degree_hist = np.array(degree_hist, dtype=float)
    degree_prob = degree_hist / G.number_of_nodes()
    
    plt.figure()
    if log_scale:
        plt.loglog(np.arange(degree_prob.shape[0]), degree_prob, 'b.')
    else:
        plt.plot(np.arange(degree_prob.shape[0]), degree_prob, 'b.')
    plt.xlabel('k')
    plt.ylabel('p(k)')
    plt.title(title)

plot_degree_dist(G1, title='Degree Distribution - Graph 1')
plt.savefig('DegDistG1.png')
plt.show()
plot_degree_dist(G2, title='Degree Distribution - Graph 2', log_scale=True)
plt.savefig('DegDistG2.png')
plt.show()


def er_predictions(G):
    n = G.number_of_nodes()
    m = G.number_of_edges()
    p = m / (n * (n - 1) / 2)   # estimated edge probability
    avg_k = p * (n - 1)          # ER predicted average degree
    std_k = np.sqrt(p * (1 - p) * (n - 1))  # ER predicted std
    max_k = avg_k + 4 * std_k    # rough estimate of max (~4 sigma)
    print(f"ER predictions for n={n}, p={p:.4f}:")
    print(f"  Predicted avg degree: {avg_k:.2f}")
    print(f"  Predicted std: {std_k:.2f}")
    print(f"  Rough predicted max degree: {max_k:.2f}")

er_predictions(G1)
er_predictions(G2)

# Average degree of an undirected graph k = 2*number of edges/number of nodes
def average_deg(graph):
    k = 2 * float(len(graph.edges)) / float(len(graph.nodes))
    print(f'Average degree is {k}')

def max_degrees(G):
    degrees = [val for (node, val) in G.degree()]
    nodes = [node for (node, val) in G.degree()]
    maximum = max(degrees)
    return (nodes[degrees.index(maximum)], maximum)

def standard_deviation(G) :
    degrees = [val for (node, val) in G.degree()]
    sd = np.std(degrees)
    return (sd)



print("Graph 1:")
average_deg(G1)
print(f' Maximum degree is for node{ max_degrees(G1)[0]} with degree { max_degrees(G1)[1]} ')
print(f'SD is {standard_deviation(G1)}')

print("Graph 2:")
average_deg(G2)
print(f' Maximum degree is for node{ max_degrees(G2)[0]} with degree { max_degrees(G2)[1]} ')
print(f'SD is {standard_deviation(G2)}')
#standard deviation



# (b)

nx.draw(G1, with_labels=True)
plt.savefig('LayoutG1.png')
plt.show()
nx.draw(G2, with_labels=True)
plt.savefig('LayoutG2.png')