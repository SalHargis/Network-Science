import networkx as nx
import matplotlib.pyplot as plt
import csv
import pandas as pd
import seaborn as sns

# Path to the dataset
raw_data_path = "/Users/sal/PycharmProjects/NetworkScience/RawData/facebook_combined.txt"

# Load the graph
with open(raw_data_path, 'r') as f:  # Open the file in read mode
    G = nx.read_edgelist(
        f,
        create_using=nx.DiGraph(),  # Create a directed graph
        nodetype=int  # Ensure node labels are integers
    )

# How many nodes and edges the graph has
print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

########## Compute Node Measures ################

degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
pagerank_centrality = nx.pagerank(G, alpha=0.85)
clustering_coefficient = nx.clustering(G.to_undirected())  # Clustering is for undirected graphs
# Ensure the graph is strongly connected or can handle exceptions
try:
    eigenvector_centrality = nx.eigenvector_centrality(G)
except nx.PowerIterationFailedConvergence:
    print("Eigenvector centrality did not converge for this graph.")
    eigenvector_centrality = {}

# Combine all measures into a dictionary for easier processing
node_measures = {}
for node in G.nodes:
    node_measures[node] = {
        "degree_centrality": degree_centrality.get(node, 0),
        "closeness_centrality": closeness_centrality.get(node, 0),
        "betweenness_centrality": betweenness_centrality.get(node, 0),
        "eigenvector_centrality": eigenvector_centrality.get(node, 0),
        "pagerank_centrality": pagerank_centrality.get(node, 0),
        "clustering_coefficient": clustering_coefficient.get(node, 0),
    }
########## Save the measures to a file ##############

# Save the results to a file
output_file = "/Users/sal/PycharmProjects/NetworkScience/Results/Facebook_node_measures.csv"

with open(output_file, 'w', newline='') as csvfile:
    fieldnames = [
        "node",
        "degree_centrality",
        "closeness_centrality",
        "betweenness_centrality",
        "eigenvector_centrality",
        "pagerank_centrality",
        "clustering_coefficient",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for node, measures in node_measures.items():
        row = {"node": node, **measures}
        writer.writerow(row)

print(f"Node measures saved to {output_file}")


######### Analyze Correlations ############

# Load the calculated graph measures
df = pd.read_csv(output_file)

# Compute the graph measure correlations
correlation_matrix = df.iloc[:, 1:].corr()  # Exclude the "node" column
print("Correlation Matrix:")
print(correlation_matrix)

# Visualize correlations with a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix of Centrality Metrics")
plt.show()