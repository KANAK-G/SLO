import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime, timedelta

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

df['Date'] = pd.to_datetime(df['Date'])

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

# Iterate over each metric and plot a separate chart
for metric in metrics:
    # Plotting
    fig, axes = plt.subplots(len(data_products), 1, figsize=(12, len(data_products) * 5), sharex=True)
    fig.suptitle(f'{metric} - True/False Occurrences (Last 7 Days)', fontsize=16)
    
    for idx, data_product in enumerate(data_products):
        # Filter data for the current data product
        df_product = final_df_last_7_days[final_df_last_7_days['Data Product Name'] == data_product]
        
        # Initialize lists to store bar plot data
        dates = []
        true_counts = []
        false_counts = []
        
        # Iterate over each date and calculate counts of True and False for the metric
        for date in df_product['Date'].unique():
            subset = df_product[df_product['Date'] == date]
            true_count = subset[metric].sum()
            false_count = len(subset) - true_count  # Assuming only True and False values
            
            dates.append(date)
            true_counts.append(true_count)
            false_counts.append(false_count)
        
        # Plot bars
        width = 0.35  # Width of the bars
        ax = axes[idx]
        ax.bar(dates, true_counts, width, label='True', color='blue')
        ax.bar(dates, false_counts, width, bottom=true_counts, label='False', color='red')
        
        # Set labels and title for each subplot
        ax.set_xlabel('Date')
        ax.set_ylabel('Count')
        ax.set_title(f'{data_product} - {metric} True/False Counts')
        ax.legend()
        ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
        ax.tick_params(axis='x', rotation=45)
    
    # Adjust layout
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

    
    # Display plot in Streamlit
    st.pyplot(fig)

