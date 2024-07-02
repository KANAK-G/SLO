import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate date range for two months
start_date = datetime.now() - timedelta(days=60)
end_date = datetime.now()
date_range = pd.date_range(start_date, end_date)

# Define data product names and dataset names
data_products = ['sales360', 'device360', 'customer360', 'store360']
dataset_names = {
    'sales360': ['sales360_dataset_1', 'sales360_dataset_2'],
    'device360': ['device360_dataset_1', 'device360_dataset_2'],
    'customer360': ['customer360_dataset_1', 'customer360_dataset_2'],
    'store360': ['store360_dataset_1', 'store360_dataset_2']
}

# Initialize an empty list to store dataframes
dfs = []

# Generate mock data for each data product and dataset
for data_product in data_products:
    for dataset_name in dataset_names[data_product]:
        data = {
            'Data Product Name': [data_product] * len(date_range),
            'Dataset Name': [dataset_name] * len(date_range),
            'Date': date_range,
            'Freshness': np.random.choice(['Pass', 'Fail'], size=len(date_range), p=[0.95, 0.05]),
            'Volume': np.random.choice(['Pass', 'Fail'], size=len(date_range), p=[0.98, 0.02]),
            'Schema': np.random.choice(['Pass', 'Fail'], size=len(date_range), p=[0.99, 0.01]),
            'Field Health': np.random.choice(['Pass', 'Fail'], size=len(date_range), p=[0.99, 0.01])  # Varying probabilities
        }

        # Convert data dictionary to DataFrame
        df = pd.DataFrame(data)

        # Append dataframe to the list
        dfs.append(df)

# Concatenate all dataframes into a single dataframe
final_df = pd.concat(dfs, ignore_index=True)

# Set up seaborn style
sns.set(style="whitegrid")

# Filter data for the last 7 days
last_7_days_filter = (datetime.now() - timedelta(days=7)) <= final_df['Date']
final_df_last_7_days = final_df[last_7_days_filter]

# Metrics to plot
metrics = ['Freshness', 'Volume', 'Schema', 'Field Health']

# Define colors based on conditions
colors = {
    'Pass': 'blue',
    'Fail': 'red'
}

# Streamlit app
st.title('Pass/Fail Metrics in Last 7 Days')

for metric in metrics:
    st.header(f'{metric} - Pass/Fail Occurrences (Last 7 Days)')
    fig, axes = plt.subplots(len(data_products), len(dataset_names[data_products[0]]), figsize=(20, 12), sharex=True, sharey=True)
    fig.suptitle(f'{metric} - Pass/Fail Occurrences (Last 7 Days)', fontsize=16)

    for i, data_product in enumerate(data_products):
        for j, dataset_name in enumerate(dataset_names[data_product]):
            # Filter data for the current data product and dataset
            df_subset = final_df_last_7_days[(final_df_last_7_days['Data Product Name'] == data_product) &
                                             (final_df_last_7_days['Dataset Name'] == dataset_name)]

            # Group by date and count Pass/Fail values for the metric
            grouped = df_subset.groupby('Date')[metric].value_counts().unstack(fill_value=0)

            # Plot bars for Pass and Fail
            dates = grouped.index
            pass_counts = grouped['Pass']
            fail_counts = grouped['Fail'] if 'Fail' in grouped.columns else pd.Series(0, index=dates)  # Handle case where there are no Fail values

            width = 0.35
            ax = axes[i, j]
            ax.bar(dates, pass_counts, width, label='Pass', color='blue', alpha=0.6)
            ax.bar(dates, fail_counts, width, bottom=pass_counts, label='Fail', color='red', alpha=0.6)

            # Set labels and title for each subplot
            ax.set_xlabel('Date')
            ax.set_ylabel('Count')
            ax.set_title(f'{data_product} - {dataset_name} - {metric} Pass/Fail Counts')
            ax.legend()
            ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
            ax.tick_params(axis='x', rotation=45)

    # Display plot in Streamlit
    st.pyplot(fig)

# Display the Streamlit app
