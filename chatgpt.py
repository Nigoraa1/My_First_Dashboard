import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = 'main_.csv'  # Update this path to your actual file location

@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    data['Combined Category'] = data['Resource Allocation'].astype(str) + '_' + data['Mental Fatigue Score'].astype(str) + '_' + data['Designation'].astype(str)
    data['Date of Joining'] = pd.to_datetime(data['Date of Joining'])  # Ensure the date column is in datetime format
    data['Season'] = data['Date of Joining'].dt.month.apply(get_season)
    data['Gender_Male'] = (data['Gender'] == 'Male').astype(int)
    data['Gender_Female'] = (data['Gender'] == 'Female').astype(int)
    return data

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Fall'

data = load_data(file_path)

# Streamlit app
st.title("Data Analysis and Visualization")

# Display the dataframe
st.header("Data Overview")
st.write(data.head())

# Display descriptive statistics
st.header("Descriptive Statistics")
st.write(data.describe())

# Separate the data into Service and Product groups
service_data = data[data['Category'] == 'Service']
product_data = data[data['Category'] == 'Product']

# Calculate average Burn Rate and Resource Allocation by Season for Service
avg_burn_rate_by_season_service = service_data.groupby('Season')['Burn Rate'].mean()
avg_resource_allocation_by_season_service = service_data.groupby('Season')['Resource Allocation'].mean()

# Calculate average Burn Rate and Resource Allocation by Season for Product
avg_burn_rate_by_season_product = product_data.groupby('Season')['Burn Rate'].mean()
avg_resource_allocation_by_season_product = product_data.groupby('Season')['Resource Allocation'].mean()

st.header("Burn Rate and Resource Allocation by Season")

# Plotting the line plots side by side for Service
fig, ax = plt.subplots(1, 2, figsize=(18, 9))

# Line plot for Burn Rate by Season for Service
ax[0].plot(avg_burn_rate_by_season_service.index, avg_burn_rate_by_season_service.values, marker='o', linestyle='-', label='Burn Rate')
ax[0].plot(avg_resource_allocation_by_season_service.index, avg_resource_allocation_by_season_service.values, marker='o', linestyle='-', label='Resource Allocation')
ax[0].set_title('Service: Burn Rate and Resource Allocation by Season')
ax[0].set_xlabel('Season')
ax[0].set_ylabel('Average Value')
ax[0].grid(True)
ax[0].legend()

# Line plot for Burn Rate by Season for Product
ax[1].plot(avg_burn_rate_by_season_product.index, avg_burn_rate_by_season_product.values, marker='o', linestyle='-', label='Burn Rate')
ax[1].plot(avg_resource_allocation_by_season_product.index, avg_resource_allocation_by_season_product.values, marker='o', linestyle='-', label='Resource Allocation')
ax[1].set_title('Product: Burn Rate and Resource Allocation by Season')
ax[1].set_xlabel('Season')
ax[1].set_ylabel('Average Value')
ax[1].grid(True)
ax[1].legend()

st.pyplot(fig)

# Display the updated dataframe with the Season column
st.header("Data with Season Column")
st.write(data.head())

# Create a heat map of the correlations
st.header("Heat Map of Correlations")

# Calculate the correlation matrix for specified columns
cols = ['Designation', 'Resource Allocation', 'Mental Fatigue Score', 'Burn Rate', 'Gender_Male', 'Gender_Female']
correlation_matrix = data[cols].corr()

# Plot the heat map
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', ax=ax)
ax.set_title('Correlation Heat Map')
st.pyplot(fig)
