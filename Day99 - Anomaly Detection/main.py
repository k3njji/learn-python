import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from scipy.spatial.distance import mahalanobis
import warnings
warnings.filterwarnings('ignore')

# ============================================
# 1. DATA LOADING & INITIAL EXPLORATION
# ============================================

# Load datasets
datasetone = pd.read_csv("energy1.csv")
datasettwo = pd.read_csv("energy2.csv")

print("Dataset One - First 5 rows:")
print(datasetone.head())

# Unique countries in first dataset
unique_name_one = datasetone['name'].unique()
print(f"\nTotal Countries of the First Dataset: {len(unique_name_one)}")

# Column names and data types
print("\nColumn Names and Corresponding Data Types:")
for col in datasetone.columns:
    print(f"{col}: {datasetone[col].dtype}")

# Second dataset exploration
unique_name_two = datasettwo['Country'].unique()
unique_year_two = datasettwo['Year'].unique()
print(f"\nTotal Countries of the Second Dataset: {len(unique_name_two)}")
print(f"Unique years in second dataset: {unique_year_two[:10]}... (showing first 10)")

print("\nDataset Two - First 5 rows:")
print(datasettwo.head())

print("\nColumn Names and Data Types for Dataset Two:")
for col in datasettwo.columns:
    print(f"{col}: {datasettwo[col].dtype}")

# ============================================
# 2. FILTERING TO 2016 ONLY
# ============================================

datasettwo = datasettwo[datasettwo['Year'] == 2016]
print(f"\nDataset Two after filtering to 2016: {len(datasettwo)} rows")

# ============================================
# 3. FINDING COMMON COUNTRIES
# ============================================

unique_values_one = set(datasetone['name'].unique())
unique_values_second = set(datasettwo['Country'].unique())

difference_one = unique_values_one - unique_values_second
difference_two = unique_values_second - unique_values_one

print(f"\nValues in datasetone but not in datasetsecond ({len(difference_one)}):")
if len(difference_one) > 0:
    print(list(difference_one)[:10])  # Show first 10

print(f"\nValues in datasetsecond but not in datasetone ({len(difference_two)}):")
if len(difference_two) > 0:
    print(list(difference_two)[:10])  # Show first 10

# Filter to common countries
datasetone_filtered = datasetone[datasetone['name'].isin(unique_values_second)]
datasettwo_filtered = datasettwo[datasettwo['Country'].isin(unique_values_one)]

print(f"\nFiltered Dataset One size: {len(datasetone_filtered)}")
print(f"Filtered Dataset Two size: {len(datasettwo_filtered)}")

# ============================================
# 4. RESHAPING DATA (CORRECTED VERSION)
# ============================================

# First, ensure we have the correct energy types mapping
energy_types = datasettwo_filtered['Energy_type'].unique()
print(f"\nEnergy types found: {energy_types}")

# Helper function to safely extract values for specific energy type
def get_values_by_type(df, column_name, energy_type):
    """Extract values for a specific energy type"""
    mask = df['Energy_type'] == energy_type
    if mask.any():
        return df.loc[mask, column_name].values[0]
    return 0

# Create a function to reshape the data
def reshape_energy_data(df):
    """Reshape from long to wide format"""
    results = []
    
    # Group by Country
    for country in df['Country'].unique():
        country_data = df[df['Country'] == country]
        
        # Base values (same for all energy types)
        base_row = {
            'Country': country,
            'Year': country_data['Year'].iloc[0],
            'GDP': country_data['GDP'].iloc[0] if len(country_data) > 0 else np.nan,
            'Population': country_data['Population'].iloc[0] if len(country_data) > 0 else np.nan,
            'Energy_intensity_per_capita': country_data['Energy_intensity_per_capita'].iloc[0] if len(country_data) > 0 else np.nan,
            'Energy_intensity_by_GDP': country_data['Energy_intensity_by_GDP'].iloc[0] if len(country_data) > 0 else np.nan,
        }
        
        # Add consumption by type
        for energy_type in energy_types:
            consumption = get_values_by_type(country_data, 'Energy_consumption', energy_type)
            production = get_values_by_type(country_data, 'Energy_production', energy_type)
            co2 = get_values_by_type(country_data, 'CO2_emission', energy_type)
            
            # Clean energy type name for column naming
            clean_type = energy_type.replace('_n_others', '_renewables').replace('petroleum_n_other_liquids', 'petroleum')
            
            base_row[f'Energy_consumption_{clean_type}'] = consumption
            base_row[f'Energy_production_{clean_type}'] = production
            base_row[f'CO2_emission_{clean_type}'] = co2
        
        results.append(base_row)
    
    return pd.DataFrame(results)

# Reshape the data
reshaped_data = reshape_energy_data(datasettwo_filtered)

print("\nReshaped Data - First 5 rows:")
print(reshaped_data.head())
print(f"\nReshaped data shape: {reshaped_data.shape}")

# ============================================
# 5. MERGING DATASETS
# ============================================

# Merge based on country name
merged_data = pd.merge(datasetone_filtered, reshaped_data, 
                       left_on='name', right_on='Country', how='left')
merged_data = merged_data.drop('Country', axis=1)

print(f"\nMerged dataset shape: {merged_data.shape}")
print("\nMerged Data - First 5 columns preview:")
print(merged_data.iloc[:, :8].head())

# ============================================
# 6. CHECKING MISSING VALUES
# ============================================

total_rows = len(merged_data)
null_counts = merged_data.isnull().sum()
null_percentage = (null_counts / total_rows) * 100

null_summary = pd.DataFrame({
    'Column': null_counts.index,
    'NullCount': null_counts.values,
    'TotalRows': total_rows,
    'NullPercentage': np.round(null_percentage, 2)
})
null_summary = null_summary[null_summary['NullCount'] > 0].sort_values('NullPercentage', ascending=False)

print("\nMissing Values Summary:")
if len(null_summary) > 0:
    print(null_summary.to_string())
else:
    print("No missing values found!")

# ============================================
# 7. PREPROCESSING - REMOVING COLUMNS
# ============================================

# List columns to remove (from your R code)
columns_to_remove = [
    'coal_net_imports', 'coal_net_exports', 'gas_net_imports', 'gas_net_exports',
    'oil_net_imports', 'oil_net_exports', 'Energy_consumption_renewables',
    'Energy_production_nuclear', 'coal_year', 'coal_units', 'gas_year', 'gas_units',
    'oil_year', 'oil_units', 'Energy_production_renewables', 'CO2_emission_coal',
    'CO2_emission_petroleum', 'CO2_emission_nuclear', 'CO2_emission_renewables', 'Year'
]

# Only remove columns that exist
columns_to_remove_existing = [col for col in columns_to_remove if col in merged_data.columns]
if columns_to_remove_existing:
    merged_data = merged_data.drop(columns=columns_to_remove_existing)
    print(f"\nRemoved {len(columns_to_remove_existing)} columns")

# Remove rows with any NA
rows_before = len(merged_data)
merged_data = merged_data.dropna()
print(f"Rows before removing NA: {rows_before}")
print(f"Rows after removing NA: {len(merged_data)}")

# Replace zeros with column means for numeric columns
numeric_cols = merged_data.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    mean_val = merged_data[col].mean()
    zero_count = (merged_data[col] == 0).sum()
    if zero_count > 0:
        merged_data[col] = merged_data[col].replace(0, mean_val)
        # print(f"  {col}: replaced {zero_count} zeros with mean ({mean_val:.2f})")

# ============================================
# 8. SAVE COUNTRY NAMES & NORMALIZATION
# ============================================

# Save country names
country_names = merged_data['name'].copy()
merged_data_numeric = merged_data.drop('name', axis=1)

# Convert percentage strings to decimal
for col in merged_data_numeric.columns:
    if merged_data_numeric[col].dtype == 'object':
        try:
            merged_data_numeric[col] = pd.to_numeric(
                merged_data_numeric[col].astype(str).str.replace('%', ''), errors='coerce'
            ) / 100
            print(f"Converted {col} from percentage to decimal")
        except:
            pass

# Normalize using Min-Max scaling
scaler = MinMaxScaler()
normalized_array = scaler.fit_transform(merged_data_numeric)
normalized_array = normalized_array * 2  # Scale to [0,2] following R code

normalized_df = pd.DataFrame(normalized_array, columns=merged_data_numeric.columns)

print(f"\nNormalized data shape: {normalized_df.shape}")
print("\nNormalized Data - First 5 rows:")
print(normalized_df.head())

# ============================================
# 9. CORRELATION MATRIX
# ============================================

correlation_matrix = normalized_df.corr()

plt.figure(figsize=(12, 10))
sns.clustermap(correlation_matrix, cmap='RdBu', center=0, 
               annot=False, fmt='.2f', linewidths=0.5, 
               figsize=(12, 10), dendrogram_ratio=0.2)
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# ============================================
# 10. MANUAL FEATURE REMOVAL
# ============================================

columns_to_remove_final = [
    're_nuclear', 'oil_consump', 'gas_consump', 'coal_consump',
    'co2_emiss_one_year_change', 'coal_exports', 'non_renewable',
    'Energy_intensity_by_GDP', 'co2_emiss_per_capita', 'pc_yearly_btu',
    'Energy_intensity_per_capita', 'oil_reserves', 'population_2016',
    'oil_imports', 'Energy_consumption_petroleum', 'co2_emissions_tons_2016',
    'country_share_of_world_co2', 'world_share', 'Energy_consumption_coal',
    'Energy_production_coal', 'Energy_consumption_natural_gas',
    'Energy_production_natural_gas', 'CO2_emission_natural_gas',
    'Energy_consumption_nuclear', 'Energy_consumption_petroleum'
]

# Only remove columns that exist
columns_to_remove_final = [col for col in columns_to_remove_final if col in normalized_df.columns]
if columns_to_remove_final:
    normalized_df = normalized_df.drop(columns=columns_to_remove_final)
    print(f"\nRemoved {len(columns_to_remove_final)} redundant columns")
    print(f"Remaining features: {normalized_df.shape[1]}")

# ============================================
# 11. FINAL DATASET WITH COUNTRY NAMES
# ============================================

final_data = pd.concat([country_names.reset_index(drop=True), 
                        normalized_df.reset_index(drop=True)], axis=1)
final_data.columns = ['name'] + list(normalized_df.columns)

print("\nFinal Dataset Preview:")
print(final_data.head())
print(f"\nFinal dataset shape: {final_data.shape}")

# ============================================
# 12. MAHALANOBIS DISTANCE FUNCTION
# ============================================

def mahalanobis_anomaly_detection(data, percentile=0.99):
    """Detect anomalies using Mahalanobis distance"""
    data_matrix = data.values if isinstance(data, pd.DataFrame) else data
    
    mean_vector = np.mean(data_matrix, axis=0)
    cov_matrix = np.cov(data_matrix, rowvar=False)
    cov_matrix_inv = np.linalg.pinv(cov_matrix)
    
    distances = np.array([mahalanobis(x, mean_vector, cov_matrix_inv) 
                          for x in data_matrix])
    
    df = data_matrix.shape[1]
    threshold = np.sqrt(chi2.ppf(percentile, df))
    anomalies = distances > threshold
    
    return distances, anomalies, threshold

# ============================================
# 13. ANOMALY DETECTION - ORIGINAL SPACE
# ============================================

mahalanobis_distances, anomalies, threshold = mahalanobis_anomaly_detection(normalized_df)
anomalous_countries = final_data['name'][anomalies].values

print("\n" + "="*60)
print("ANOMALY DETECTION - ORIGINAL SPACE")
print("="*60)
print(f"Number of features: {normalized_df.shape[1]}")
print(f"Threshold: {threshold:.4f}")
print(f"Detected {sum(anomalies)} anomalies ({sum(anomalies)/len(anomalies)*100:.1f}%)")
print(f"Anomalous countries: {list(anomalous_countries)}")

# ============================================
# 14. PCA ANALYSIS
# ============================================

pca = PCA(n_components=3, random_state=42)
pca_result = pca.fit_transform(normalized_df)

print("\n" + "="*60)
print("PCA RESULTS")
print("="*60)
print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
print(f"Cumulative explained variance: {sum(pca.explained_variance_ratio_)*100:.2f}%")

pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2', 'PC3'])
final_data_pca = pd.concat([country_names.reset_index(drop=True), pca_df], axis=1)

print("\nPCA Data - First 5 rows:")
print(final_data_pca.head())

# ============================================
# 15. ANOMALY DETECTION - PCA SPACE
# ============================================

pca_distances, pca_anomalies, pca_threshold = mahalanobis_anomaly_detection(pca_result)
pca_anomalous_countries = final_data['name'][pca_anomalies].values

print("\n" + "="*60)
print("ANOMALY DETECTION - PCA SPACE")
print("="*60)
print(f"Number of components: {pca_result.shape[1]}")
print(f"Threshold: {pca_threshold:.4f}")
print(f"Detected {sum(pca_anomalies)} anomalies ({sum(pca_anomalies)/len(pca_anomalies)*100:.1f}%)")
print(f"Anomalous countries: {list(pca_anomalous_countries)}")

# ============================================
# 16. VISUALIZATIONS
# ============================================

# Histogram for original space
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

axes[0].hist(mahalanobis_distances, bins=30, color='steelblue', alpha=0.7, edgecolor='black')
axes[0].axvline(threshold, color='red', linestyle='--', linewidth=2, label=f'Threshold ({threshold:.2f})')
axes[0].set_xlabel('Mahalanobis Distance')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Mahalanobis Distance Distribution - Original Space')
axes[0].legend()

# Histogram for PCA space
axes[1].hist(pca_distances, bins=30, color='coral', alpha=0.7, edgecolor='black')
axes[1].axvline(pca_threshold, color='red', linestyle='--', linewidth=2, label=f'Threshold ({pca_threshold:.2f})')
axes[1].set_xlabel('Mahalanobis Distance')
axes[1].set_ylabel('Frequency')
axes[1].set_title('Mahalanobis Distance Distribution - PCA Space')
axes[1].legend()

plt.tight_layout()
plt.show()

# PCA scatter plot
plt.figure(figsize=(10, 8))
colors = ['red' if a else 'steelblue' for a in pca_anomalies]
plt.scatter(pca_df['PC1'], pca_df['PC2'], c=colors, alpha=0.7, s=100, edgecolors='black')

# Label anomalies
for i, (idx, row) in enumerate(final_data_pca[pca_anomalies].iterrows()):
    plt.annotate(row['name'], (row['PC1'], row['PC2']), 
                 xytext=(5, 5), textcoords='offset points',
                 fontsize=9, fontweight='bold', color='red')

plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)')
plt.title('PCA Projection with Anomaly Detection')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ============================================
# 17. SUMMARY STATISTICS
# ============================================

print("\n" + "="*60)
print("FINAL SUMMARY")
print("="*60)
print(f"Number of countries analyzed: {len(final_data)}")
print(f"Number of features after preprocessing: {normalized_df.shape[1]}")
print(f"Number of anomalies (original space): {sum(anomalies)}")
print(f"Number of anomalies (PCA space): {sum(pca_anomalies)}")

common_anomalies = set(anomalous_countries) & set(pca_anomalous_countries)
print(f"Common anomalies detected by both methods: {len(common_anomalies)}")
if common_anomalies:
    print(f"Countries: {sorted(common_anomalies)}")