import networkx as nx
import numpy as np
import math
from collections import defaultdict, Counter

# metis file parsing
def read_metis_graph(metis_graph_file):
    """ Reads a METIS adjacency-list graph file and returns a NetworkX graph. """
    G = nx.Graph()
    
    with open(metis_graph_file, 'r') as f:
        lines = f.readlines()
        num_nodes, _ = map(int, lines[0].strip().split())  # First line: num_nodes, num_edges
        
        for node_id, line in enumerate(lines[1:], start=1):  # Nodes start from 1
            neighbors = map(int, line.strip().split())  # Read neighbors
            for neighbor in neighbors:
                G.add_edge(node_id, neighbor)  # Add edges

    return G

def read_metis_partition(metis_partition_file):
    """ Reads a METIS partition file and returns a dictionary mapping nodes to their detected communities. """
    detected_communities = {}
    
    with open(metis_partition_file, 'r') as f:
        for node_id, line in enumerate(f, start=1):  # Nodes are 1-based
            community = int(line.strip())  # Community ID
            detected_communities[node_id] = community
    
    return detected_communities

# ground truth parsing
def parse_ground_truth(file_path):
    """ Reads the ground truth file and returns a dictionary mapping nodes to their true community. """
    ground_truth = {}
    with open(file_path, 'r') as f:
        for community_id, line in enumerate(f):
            nodes = list(map(int, line.strip().split()))
            for node in nodes:
                ground_truth[node] = community_id  # Assign a community label
    return ground_truth

# Calculate entropy
def calculate_entropy(graph, detected_communities, ground_truth):
    """ Computes entropy for the subset of nodes with ground truth. """
    # Filter nodes that exist in all three: graph, detected communities, and ground truth
    filtered_nodes = set(ground_truth.keys()) & set(detected_communities.keys()) & set(graph.nodes)

    # Map ground truth community to detected community distributions
    gt_to_detected = {gt: Counter() for gt in set(ground_truth.values())}
    
    for node in filtered_nodes:
        gt_label = ground_truth[node]
        detected_label = detected_communities[node]
        gt_to_detected[gt_label][detected_label] += 1

    # Compute entropy per ground truth community
    entropy_values = []
    for gt_label, detected_counts in gt_to_detected.items():
        total = sum(detected_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in detected_counts.values())
        entropy_values.append(entropy)

    return np.mean(entropy_values) if entropy_values else 0.0

# main function
def compute_entropy(metis_graph_file, ground_truth_file, *metis_partition_files):
    """ Computes entropy for the ground truth subset of the YouTube dataset. """
    G = read_metis_graph(metis_graph_file)  # Load METIS graph
    ground_truth = parse_ground_truth(ground_truth_file)  # Load ground truth

    results = {}
    
    for partition_file in metis_partition_files:
        detected_communities = read_metis_partition(partition_file)  # Load detected communities

        # Compute entropy
        entropy_score = calculate_entropy(G, detected_communities, ground_truth)

        results[partition_file] = {"entropy": entropy_score}

        print(f"\nResults for {partition_file}:")
        print(f"  Entropy Score: {entropy_score}")

    return results

# Paths to files (update accordingly)
metis_graph_file = "/home/hargis.29/CSE5245/Lab2/CommDetectExe/com-youtube.ungraph.metis"
ground_truth_file = "/home/hargis.29/CSE5245/Lab2/CommDetectExe/com-youtube.all.cmty.GT"

compute_entropy(
    metis_graph_file,
    ground_truth_file,
    "/home/hargis.29/CSE5245/Lab2/ResultsGPMetis/com-youtube.ungraph.metis.part.2500",
    "/home/hargis.29/CSE5245/Lab2/ResultsMLRMCL/com-youtube.ungraph.metis.c1000.i2.0.b0.5"
)



