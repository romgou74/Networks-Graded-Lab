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

# Average degree of an undirected graph k = 2*number of edges/number of nodes

print(len(G1.edges))

def average_deg(graph):
    k = 2 * float(len(graph.edges)) / float(len(graph.nodes))
    print(k)

average_deg(G1)
average_deg(G2)