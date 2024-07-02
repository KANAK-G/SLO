import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# Define data product names and dataset names
data_products = ['sales360', 'device360', 'customer360', 'store360']

# Load the mock data
df = pd.read_csv('slo_data.csv')

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
            df_subset = df[(df['Data Product Name'] == data_product) &
                                             (df['Dataset Name'] == dataset_name)]

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
