import networkx as nx
from collections import defaultdict

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
    """ Reads a METIS partition file and returns community groupings. """
    community_dict = defaultdict(set)
    
    with open(metis_partition_file, 'r') as f:
        for node_id, line in enumerate(f, start=1):  # Nodes are 1-based
            community = int(line.strip())  # Community ID
            community_dict[community].add(node_id)
    
    return list(community_dict.values())

def compute_conductance(G, communities):
    """ Computes the average conductance of the given communities in the graph G. """
    conductance_values = []
    
    for community in communities:
        cut_size = sum(1 for node in community for neighbor in G.neighbors(node) if neighbor not in community)
        volume = sum(1 for node in community for _ in G.neighbors(node))
        
        if volume > 0:
            conductance_values.append(cut_size / min(volume, 2 * (len(G) - len(community))))
    
    return sum(conductance_values) / len(conductance_values)

def compute_ncut(G, communities):
    """ Computes the normalized cut score for the given partition. """
    total_ncut = 0
    
    for community in communities:
        cut_size = sum(1 for node in community for neighbor in G.neighbors(node) if neighbor not in community)
        volume = sum(1 for node in community for _ in G.neighbors(node))
        complement_volume = sum(1 for node in (G.nodes - community) for _ in G.neighbors(node))
        
        if volume > 0 and complement_volume > 0:
            total_ncut += (cut_size / volume) + (cut_size / complement_volume)
    
    return total_ncut / len(communities)

def compute_metrics(metis_graph_file, *metis_partition_files):
    """ Computes and compares modularity, conductance, and normalized cut for multiple METIS partitionings. """
    G = read_metis_graph(metis_graph_file)  # Load METIS graph
    
    results = {}
    
    for partition_file in metis_partition_files:
        communities = read_metis_partition(partition_file)  # Load partitions

        # Ensure all community nodes exist in the graph
        graph_nodes = set(G.nodes)
        filtered_communities = [group & graph_nodes for group in communities]

        # Compute metrics
        modularity_score = nx.community.modularity(G, filtered_communities)
        conductance_score = compute_conductance(G, filtered_communities)
        ncut_score = compute_ncut(G, filtered_communities)

        results[partition_file] = {
            "modularity": modularity_score,
            "conductance": conductance_score,
            "ncut": ncut_score
        }

        print(f"\nResults for {partition_file}:")
        print(f"  Modularity Score: {modularity_score}")
        print(f"  Conductance Score: {conductance_score}")
        print(f"  Normalized Cut (NCut) Score: {ncut_score}")

    return results

# wiki-Vote Data
compute_metrics(
    "/home/hargis.29/CSE5245/Lab2/CommDetectExe/p2p-Gnutella08.metis",
    "/home/hargis.29/CSE5245/Lab2/ResultsGPMetis/p2p-Gnutella08.metis.part.650",
    "/home/hargis.29/CSE5245/Lab2/ResultsMLRMCL/p2p-Gnutella08.metis.c1000.i2.0.b0.5"
)
