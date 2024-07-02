import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime

#Define data product names and dataset names
data_products = ['sales360', 'device360', 'customer360', 'store360']

dataset_names = {
    'sales360': ['sales360_dataset_1', 'sales360_dataset_2'],
    'device360': ['device360_dataset_1', 'device360_dataset_2'],
    'customer360': ['customer360_dataset_1', 'customer360_dataset_2'],
    'store360': ['store360_dataset_1', 'store360_dataset_2']
}


# Load the mock data
df = pd.read_csv('slo_data.csv')

# Metrics to plot
metrics = ['Freshness', 'Volume', 'Schema', 'Field Health']

# Define colors based on conditions
colors = {
    'Pass': 'blue',
    'Fail': 'red'
}

# Display the Streamlit app


# Filter data for the last 7 days
last_7_days_filter = (datetime.now() - timedelta(days=7)) <= df['Date']
final_df_last_7_days = df[last_7_days_filter]

# Metrics to plot
metrics = ['Freshness', 'Volume', 'Schema', 'Field Health']

# Define colors based on conditions
colors = {
    True: 'blue',
    False: 'red'
}


# Streamlit app
st.title('Pass/Fail Metrics in Last 7 Days')

sns.set(style="whitegrid")

# Iterate over each metric and plot a separate chart for each dataset within each data product
for metric in metrics:
    # Plotting
    fig, axes = plt.subplots(len(data_products), len(dataset_names[data_products[0]]), figsize=(20, 12), sharex=True, sharey=True)
    fig.suptitle(f'{metric} - True/False Occurrences (Last 7 Days)', fontsize=16)
    
    for i, data_product in enumerate(data_products):
        for j, dataset_name in enumerate(dataset_names[data_product]):
            # Filter data for the current data product and dataset
            df_subset = final_df_last_7_days[(final_df_last_7_days['Data Product Name'] == data_product) &
                                             (final_df_last_7_days['Dataset Name'] == dataset_name)]
            
            # Group by date and count True/False values for the metric
            grouped = df_subset.groupby('Date')[metric].value_counts().unstack(fill_value=0)
            
            # Plot bars for True and False
            dates = grouped.index
            true_counts = grouped[True]
            false_counts = grouped[False] if False in grouped.columns else pd.Series(0, index=dates)  # Handle case where there are no False values
            
            width = 0.35
            ax = axes[i, j]
            ax.bar(dates, true_counts, width, label='True', color='blue', alpha=0.6)
            ax.bar(dates, false_counts, width, bottom=true_counts, label='False', color='red', alpha=0.6)
            
            # Set labels and title for each subplot
            ax.set_xlabel('Date')
            ax.set_ylabel('Count')
            ax.set_title(f'{data_product} - {dataset_name} - {metric} True/False Counts')
            ax.legend()
            ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
            ax.tick_params(axis='x', rotation=45)
    
    # Display plot in Streamlit
    st.pyplot(fig)

