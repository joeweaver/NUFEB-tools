import pandas as pd

results = pd.read_csv('gathered_sim_results.csv')
spatial = pd.read_csv('gathered_spatial_distributions.csv')
sizes = pd.read_csv('gathered_atom_sizes.csv')

spatial_results = pd.merge(spatial, results)

fully_combined = pd.merge(spatial_results, sizes, how='left',
                          left_on=['RunID', 'seed'],
                          right_on = ['RunID', 'Atom']) \
                    .drop(columns=['Atom'])

fully_combined.to_csv('combined_gathered_results_metadata.csv')
