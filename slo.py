import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Assuming df is already created and has data

# Filter the data for the last 7 days for device360 data product
end_date = datetime.now()
start_date = end_date - timedelta(days=7)
device360_df = df[(df['data_product_name'] == 'device360') & (df['date'] >= start_date)]

datasets = device360_df['dataset_name'].unique()

# Function to plot distribution for each dataset and column
def plot_distribution(dataset, column):
    plt.figure(figsize=(14, 8))
    dataset_df = device360_df[device360_df['dataset_name'] == dataset]
    
    # Convert 'Pass' and 'Fail' to 1 and 0 for proper plotting
    dataset_df[column] = dataset_df[column].apply(lambda x: 1 if x == 'Pass' else 0)
    
    sns.histplot(data=dataset_df, x='date', hue=column, multiple='stack', bins=len(pd.date_range(start=start_date, end=end_date)),
                 palette={0: 'red', 1: 'green'}, shrink=0.8)
    plt.title(f'Distribution of {column} for {dataset} in device360 over the last 7 days')
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Pass/Fail')
    plt.legend(title=column, labels=['Pass', 'Fail'])
    plt.show()

columns_to_check = ['freshness', 'volume', 'schema', 'field_health']

for dataset in datasets:
    for column in columns_to_check:
        plot_distribution(dataset, column)


# Filter the data for the last 7 days for sales360 data product
end_date = datetime.now()
start_date = end_date - timedelta(days=7)
device360_df = df[(df['data_product_name'] == 'sales360') & (df['date'] >= start_date)]

datasets = device360_df['dataset_name'].unique()

# Function to plot distribution for each dataset and column
def plot_distribution(dataset, column):
    plt.figure(figsize=(14, 8))
    dataset_df = device360_df[device360_df['dataset_name'] == dataset]
    
    # Convert 'Pass' and 'Fail' to 1 and 0 for proper plotting
    dataset_df[column] = dataset_df[column].apply(lambda x: 1 if x == 'Pass' else 0)
    
    sns.histplot(data=dataset_df, x='date', hue=column, multiple='stack', bins=len(pd.date_range(start=start_date, end=end_date)),
                 palette={0: 'red', 1: 'green'}, shrink=0.8)
    plt.title(f'Distribution of {column} for {dataset} in sales360 over the last 7 days')
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Pass/Fail')
    plt.legend(title=column, labels=['Pass', 'Fail'])
    plt.show()

columns_to_check = ['freshness', 'volume', 'schema', 'field_health']

for dataset in datasets:
    for column in columns_to_check:
        plot_distribution(dataset, column)



# Filter the data for the last 7 days for device360 data product
end_date = datetime.now()
start_date = end_date - timedelta(days=7)
device360_df = df[(df['data_product_name'] == 'customer360') & (df['date'] >= start_date)]

datasets = device360_df['dataset_name'].unique()

# Function to plot distribution for each dataset and column
def plot_distribution(dataset, column):
    plt.figure(figsize=(14, 8))
    dataset_df = device360_df[device360_df['dataset_name'] == dataset]
    
    # Convert 'Pass' and 'Fail' to 1 and 0 for proper plotting
    dataset_df[column] = dataset_df[column].apply(lambda x: 1 if x == 'Pass' else 0)
    
    sns.histplot(data=dataset_df, x='date', hue=column, multiple='stack', bins=len(pd.date_range(start=start_date, end=end_date)),
                 palette={0: 'red', 1: 'green'}, shrink=0.8)
    plt.title(f'Distribution of {column} for {dataset} in customer360 over the last 7 days')
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Pass/Fail')
    plt.legend(title=column, labels=['Pass', 'Fail'])
    plt.show()

columns_to_check = ['freshness', 'volume', 'schema', 'field_health']

for dataset in datasets:
    for column in columns_to_check:
        plot_distribution(dataset, column)



# Filter the data for the last 7 days for device360 data product
end_date = datetime.now()
start_date = end_date - timedelta(days=7)
device360_df = df[(df['data_product_name'] == 'store360') & (df['date'] >= start_date)]

datasets = device360_df['dataset_name'].unique()

# Function to plot distribution for each dataset and column
def plot_distribution(dataset, column):
    plt.figure(figsize=(14, 8))
    dataset_df = device360_df[device360_df['dataset_name'] == dataset]
    
    # Convert 'Pass' and 'Fail' to 1 and 0 for proper plotting
    dataset_df[column] = dataset_df[column].apply(lambda x: 1 if x == 'Pass' else 0)
    
    sns.histplot(data=dataset_df, x='date', hue=column, multiple='stack', bins=len(pd.date_range(start=start_date, end=end_date)),
                 palette={0: 'red', 1: 'green'}, shrink=0.8)
    plt.title(f'Distribution of {column} for {dataset} in store360 over the last 7 days')
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Pass/Fail')
    plt.legend(title=column, labels=['Pass', 'Fail'])
    plt.show()

columns_to_check = ['freshness', 'volume', 'schema', 'field_health']

for dataset in datasets:
    for column in columns_to_check:
        plot_distribution(dataset, column)
