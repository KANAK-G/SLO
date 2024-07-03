import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt  # Ensure matplotlib.pyplot is imported

from datetime import datetime, timedelta
import streamlit as st

# Load the mock data
df = pd.read_csv('slo_data.csv')

# Convert 'date' column to datetime format if it's stored as string
df['date'] = pd.to_datetime(df['date'])

# Create separate DataFrames for each dataset
device360_df = df[df['dataset_name'].str.contains('device360')]
customer360_df = df[df['dataset_name'].str.contains('customer360')]
store360_df = df[df['dataset_name'].str.contains('store360')]
sales360_df = df[df['dataset_name'].str.contains('sales360')]

# Define the columns to select
columns = [
    'dataset_name', 
    'field_health_check_name', 
    'field_health_check_value', 
    'schema_check_name', 
    'schema_check_value', 
    'freshness_check_name', 
    'freshness_check_value', 
    'volume_check_name', 
    'volume_check_value'
]

# Create separate DataFrames for each dataset with unique values in the specified columns
device360_unique_df = device360_df[columns].drop_duplicates()
customer360_unique_df = customer360_df[columns].drop_duplicates()
store360_unique_df = store360_df[columns].drop_duplicates()
sales360_unique_df = sales360_df[columns].drop_duplicates()

# Streamlit visualizations
st.title("Unique Check Values per Data Product")

st.header("Device360 Dataset")
st.dataframe(device360_unique_df)

st.header("Customer360 Dataset")
st.dataframe(customer360_unique_df)

st.header("Store360 Dataset")
st.dataframe(store360_unique_df)

st.header("Sales360 Dataset")
st.dataframe(sales360_unique_df)


# Main Streamlit app
def main():
    st.title('Distribution of SLO status for Data Products and Datasets')
    
    # Filter data for the last 7 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    filtered_df = df[df['date'].between(start_date, end_date)]
    
    # Get unique data products
    data_products = filtered_df['data_product_name'].unique()
    
    # Dropdown to select data product
    selected_data_product = st.selectbox('Select Data Product', data_products)
    
    # Get datasets for selected data product
    datasets = filtered_df[filtered_df['data_product_name'] == selected_data_product]['dataset_name'].unique()
    
    # Dropdown to select dataset
    selected_dataset = st.selectbox('Select Dataset', datasets)
    
    # Function to plot distribution for each column
    def plot_distribution(data_df, data_product, dataset, column):
        # Ensure plt is referenced from the matplotlib.pyplot module
        plt.figure(figsize=(14, 8))
        dataset_df = data_df[(data_df['data_product_name'] == data_product) & (data_df['dataset_name'] == dataset)]
        
        # Convert 'Pass' and 'Fail' to 1 and 0 for proper plotting
        dataset_df[column] = dataset_df[column].apply(lambda x: 1 if x == 'Pass' else 0)
        
        sns.histplot(data=dataset_df, x='date', hue=column, multiple='stack', bins=len(pd.date_range(start=start_date, end=end_date)),
                     palette={0: 'red', 1: 'green'}, shrink=0.8)
        plt.title(f'Distribution of {column} for {dataset} in {data_product} over the last 7 days')
        plt.xticks(rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Pass/Fail')
        plt.legend(title=column, labels=['Pass', 'Fail'])
        
        return plt
    
    # Display plot for each column
    columns_to_check = ['freshness', 'volume', 'schema', 'field_health']
    for column in columns_to_check:
        plot = plot_distribution(filtered_df, selected_data_product, selected_dataset, column)
        st.pyplot(plot)
        st.write('\n\n')  # Add spacing between plots

if __name__ == "__main__":
    main()




