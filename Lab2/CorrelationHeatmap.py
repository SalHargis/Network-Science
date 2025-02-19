import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def compute_correlation(metrics_dict):
    """
    Computes and visualizes the correlation matrix for modularity, conductance, and normalized cut.
    """
    # Convert results dictionary to DataFrame
    df = pd.DataFrame(metrics_dict).T  # Transpose to get partitions as rows
    
    # Compute Pearson correlation
    corr_matrix = df.corr(method='pearson')
    
    # Plot heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap of Modularity, Conductance, and Normalized Cut')
    plt.show()
    
    return corr_matrix

#### Data Inputs ####

# Ca-GrQc Data:
# metrics_results = {
#     "CNM": {"modularity": 0.8160, "conductance": 0.0175, "ncut": 0.0002},
#     "MLRMCL": {"modularity": 0.7427413738676999, "conductance": 0.1738296615132966, "ncut": 0.17415314672067236},
#     "GPMetis": {"modularity": 0.3461386598176384, "conductance": 0.48873626632514905, "ncut": 0.4896096516715551}
# }

# Wiki-Vote
# metrics_results = {
#     "CNM": {"modularity": 0.3500, "conductance": 0.2612, "ncut": 0.0043},
#     "MLRMCL": {"modularity": 0.1206508812487393, "conductance": 0.8753593178095572, "ncut": 0.8659733302491168},
#     "GPMetis": {"modularity": 0.048487029894115075, "conductance": 0.9413215870672501, "ncut": 0.9438585725981377}
# }

# Facebook
# metrics_results = {
#     "CNM": {"modularity": 0.7754, "conductance": 0.1056, "ncut": 0.0021},
#     "MLRMCL": {"modularity": 0.7878440023785953, "conductance": 0.5828565500870414, "ncut": 0.5806327132336003},
#     "GPMetis": {"modularity": 0.17415142264649117, "conductance": 0.7447020280972786, "ncut": 0.7501983237745875}
# }

# Gnutella
metrics_results = {
    "CNM": {"modularity": 0.4647, "conductance": 0.4080, "ncut": 0.0175},
    "MLRMCL": {"modularity": 0.31986520043242084, "conductance": 0.6784736322096859, "ncut": 0.6795017045529197},
    "GPMetis": {"modularity": 0.1223275153833746, "conductance": 0.8623881611629702, "ncut": 0.8637381142152598}
}

correlation_matrix = compute_correlation(metrics_results)

print(correlation_matrix)
