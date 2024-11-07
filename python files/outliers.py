import pandas as pd
import numpy as np
from geopy.distance import geodesic
import sys

# Load the CSV data
file_path = 'EKITI_geocoded - EKITI_geocoded.csv.csv'
try:
    complete_data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f'Error: File {file_path} does not appear to exist.')
    sys.exit(1)
except Exception as ex:
    print(f"An error occurred: {ex}")
    sys.exit(1)

# Print the column names to verify
print(complete_data.columns)

# Extract latitude and longitude columns
lat_lon = complete_data[['Latitude', 'Longitude']].values

# Define the radius for neighbors (in kilometers)
radius_km = 1.0

# Create a function to compute the geodesic distance matrix
def geodesic_distance_matrix(locations):
    n = len(locations)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist = geodesic(locations[i], locations[j]).km
            dist_matrix[i, j] = dist
            dist_matrix[j, i] = dist
    return dist_matrix

# Compute the geodesic distance matrix
geo_dist_matrix = geodesic_distance_matrix(lat_lon)

# Create a list to store the outlier scores and neighbor information
results = []

# Iterate over each polling unit to calculate the outlier scores
for index, row in complete_data.iterrows():
    # Find neighboring polling units within the specified radius
    neighbors = complete_data[(geo_dist_matrix[index] <= radius_km) & (complete_data.index != index)]

    # Calculate the outlier score for each party
    apc_outlier = abs(row['APC'] - neighbors['APC'].mean()) if not neighbors.empty else 0
    lp_outlier = abs(row['LP'] - neighbors['LP'].mean()) if not neighbors.empty else 0
    pdp_outlier = abs(row['PDP'] - neighbors['PDP'].mean()) if not neighbors.empty else 0
    nnpp_outlier = abs(row['NNPP'] - neighbors['NNPP'].mean()) if not neighbors.empty else 0

    # Store the results
    results.append({
        'PU-Code': row['PU-Code'],
        'PU-Name': row['PU-Name'],
        'Ward': row['Ward'],
        'Latitude': row['Latitude'],
        'Longitude': row['Longitude'],
        'APC_outlier': apc_outlier,
        'LP_outlier': lp_outlier,
        'PDP_outlier': pdp_outlier,
        'NNPP_outlier': nnpp_outlier,
        'Neighbors': neighbors['PU-Code'].tolist()
    })

# Convert the results list to a DataFrame
outlier_scores = pd.DataFrame(results)

# Sort the dataset by the outlier scores for each party
sorted_apc = outlier_scores.sort_values(by='APC_outlier', ascending=False).head(3)
sorted_lp = outlier_scores.sort_values(by='LP_outlier', ascending=False).head(3)
sorted_pdp = outlier_scores.sort_values(by='PDP_outlier', ascending=False).head(3)
sorted_nnpp = outlier_scores.sort_values(by='NNPP_outlier', ascending=False).head(3)

# Save the outlier scores and sorted results to an Excel file
output_file_path = 'outlier_scores.xlsx'
with pd.ExcelWriter(output_file_path) as writer:
    outlier_scores.to_excel(writer, sheet_name='Outlier Scores', index=False)
    sorted_apc.to_excel(writer, sheet_name='Top 3 APC Outliers', index=False)
    sorted_lp.to_excel(writer, sheet_name='Top 3 LP Outliers', index=False)
    sorted_pdp.to_excel(writer, sheet_name='Top 3 PDP Outliers', index=False)
    sorted_nnpp.to_excel(writer, sheet_name='Top 3 NNPP Outliers', index=False)

# Print the output file path
print(f"The outlier scores and top 3 outliers for each party have been saved to {output_file_path}")

