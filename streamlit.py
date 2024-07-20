import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io


df = pd.read_csv("main_.csv")

st.write("# Burning out 🧠🤯")


# datasetning maqsadi haqida qisqacha ma'lumot
st.text("""Globally, World Mental Health Day is celebrated on October 10 each year. 
        The objective of this day is to raise awareness about mental health issues around 
        the world and mobilize efforts in support of mental health. According to an anonymous 
        survey, about 450 million people live with mental disorders that can be one of the primary 
        causes of poor health and disability worldwide. These days when the world is suffering from a 
        pandemic situation, it becomes really hard to maintain mental fitness.""")


# Convert 'Date of Joining' to datetime format
df['Date of Joining'] = pd.to_datetime(df['Date of Joining'])

# Function to get the season from the date
def get_season(date):
    month = date.month
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

# Apply the season function to the 'Date of Joining' column
df['Season'] = df['Date of Joining'].apply(get_season)


# Dataset
row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
with row3_1:
    st.markdown("")
    see_data = st.expander('You can click here to see the raw data first 👉')
    with see_data:
        st.dataframe(data=df.reset_index(drop=True))


buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()

st.text(s)




# Filling Missing Datas

#RESOURCE ALLOCATION COLUMN

df["moda_Resource Allocation"] = df["Resource Allocation"].fillna(df["Resource Allocation"].mode())
df["mean_Resource Allocation"] = df["Resource Allocation"].fillna(df["Resource Allocation"].mean())
df["median_Resource Allocation"] = df["Resource Allocation"].fillna(df["Resource Allocation"].median())



# Create the plots
fig1, ax1 = plt.subplots()
sns.histplot(x="Resource Allocation", data=df, kde=True, ax=ax1)
ax1.set_title('ORGINAL')

fig2, ax2 = plt.subplots()
sns.histplot(x="mean_Resource Allocation", data=df, kde=True, ax=ax2)
ax2.set_title('MEAN')

fig3, ax3 = plt.subplots()
sns.histplot(x="moda_Resource Allocation", data=df,kde=True, ax=ax3)
ax3.set_title('MODA')

fig4, ax4 = plt.subplots()
sns.histplot(x="median_Resource Allocation", data=df,kde=True, ax=ax4)
ax4.set_title('MEDIAN')


# Sidebar button
show_plots = st.sidebar.button('Resource Allocation')


# Initialize session state if it doesn't exist
if 'plots_visible' not in st.session_state:
    st.session_state.plots_visible = False


# Toggle the visibility of the plots
if show_plots:
    st.session_state.plots_visible = not st.session_state.plots_visible


if show_plots:
        st.write("#________________Filling Missing Values___________________     ")

# Conditionally display the plots
if st.session_state.plots_visible:
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.pyplot(fig1)

    with col2:
        st.pyplot(fig2)

    with col3:
        st.pyplot(fig3)

    with col4:
        st.pyplot(fig4)


df["Resource Allocation"] = df["Resource Allocation"].fillna(df["Resource Allocation"].mode())

#Drop unneeded columns
df.drop(columns="mean_Resource Allocation")
df.drop(columns="moda_Resource Allocation")
df.drop(columns="median_Resource Allocation")






#Mental Fatigue Score COLUMN
df["moda_Mental Fatigue Score"] = df["Mental Fatigue Score"].fillna(df["Mental Fatigue Score"].mode())
df["mean_Mental Fatigue Score"] = df["Mental Fatigue Score"].fillna(df["Mental Fatigue Score"].mean())
df["median_Mental Fatigue Score"] = df["Mental Fatigue Score"].fillna(df["Mental Fatigue Score"].median())


# Create the plots
fig_1, ax_1 = plt.subplots()
sns.histplot(x="Mental Fatigue Score", data=df, kde=True, ax=ax_1,color='purple')
ax1.set_title('ORGINAL')

fig_2, ax_2 = plt.subplots()
sns.histplot(x="mean_Mental Fatigue Score", data=df, kde=True, ax=ax_2,color='purple')
ax_2.set_title('MEAN')

fig_3, ax_3 = plt.subplots()
sns.histplot(x="moda_Mental Fatigue Score", data=df,kde=True, ax=ax_3,color='purple')
ax3.set_title('MODA')

fig_4, ax_4 = plt.subplots()
sns.histplot(x="median_Mental Fatigue Score", data=df,kde=True, ax=ax_4,color='purple')
ax4.set_title('MEDIAN')


# Sidebar button
show_plots = st.sidebar.button('Mental Fatigue Score')


# Initialize session state if it doesn't exist
if 'plots_visible' not in st.session_state:
    st.session_state.plots_visible = False


# Toggle the visibility of the plots
if show_plots:
    st.session_state.plots_visible = not st.session_state.plots_visible


if show_plots:
        st.write("# ________________Filling Missing Values___________________     ")
        

# Conditionally display the plots
if st.session_state.plots_visible:
    col_1, col_2 = st.columns(2)
    col_3, col_4 = st.columns(2)

    with col_1:
        st.pyplot(fig_1)

    with col_2:
        st.pyplot(fig_2)

    with col_3:
        st.pyplot(fig_3)

    with col_4:
        st.pyplot(fig_4)

df["Mental Fatigue Score"] = df["Mental Fatigue Score"].fillna(df["Mental Fatigue Score"].mode())

#Drop unneeded columns
df.drop(columns="mean_Mental Fatigue Score")
df.drop(columns="moda_Mental Fatigue Score")
df.drop(columns="median_Mental Fatigue Score")





#Burn Out Rate COLUMN
df["moda_Burn_Rate"] = df["Burn Rate"].fillna(df["Burn Rate"].mode())
df["mean_Burn_Rate"] = df["Burn Rate"].fillna(df["Burn Rate"].mean())
df["median_Burn_Rate"] = df["Burn Rate"].fillna(df["Burn Rate"].median())


# Create the plots
fig__1, ax__1 = plt.subplots()
sns.histplot(x="Burn Rate", data=df, kde=True, ax=ax__1,color='orange')
ax__1.set_title('ORGINAL')

fig__2, ax__2 = plt.subplots()
sns.histplot(x="mean_Burn_Rate", data=df, kde=True, ax=ax__2,color='orange')
ax_2.set_title('MEAN')

fig__3, ax__3 = plt.subplots()
sns.histplot(x="moda_Burn_Rate", data=df,kde=True, ax=ax__3,color='orange')
ax__3.set_title('MODA')

fig__4, ax__4 = plt.subplots()
sns.histplot(x="median_Burn_Rate", data=df,kde=True, ax=ax__4,color='orange')
ax__4.set_title('MEDIAN')


# Sidebar button
show_plotss = st.sidebar.button('Burn Rate')


# Initialize session state if it doesn't exist
if 'plots_visible' not in st.session_state:
    st.session_state.plots_visible = False


# Toggle the visibility of the plots
if show_plotss:
    st.session_state.plots_visible = not st.session_state.plots_visible


if show_plotss:
        st.write("# ________________Filling Missing Values___________________     ")

# Conditionally display the plots
if st.session_state.plots_visible:
    col__1, col__2 = st.columns(2)
    col__3, col__4 = st.columns(2)

    with col__1:
        st.pyplot(fig__1)

    with col__2:
        st.pyplot(fig__2)

    with col__3:
        st.pyplot(fig__3)

    with col__4:
        st.pyplot(fig__4)



df["Burn Rate"] = df["Burn Rate"].fillna(df["Burn Rate"].mode())

#Drop unneeded columns
df.drop(columns="mean_Burn_Rate")
df.drop(columns="moda_Burn_Rate")
df.drop(columns="median_Burn_Rate")






# 'WFH Setup Available' 'Yes' bo'lganda filtrlash
filtered_data = df[df['WFH Setup Available'] == 'Yes']

# Erkaklar va ayollar uchun alohida barplot yaratish
male_data = filtered_data[filtered_data['Gender'] == 'Male']
female_data = filtered_data[filtered_data['Gender'] == 'Female']





# Filter by Gender
gender_filter = st.sidebar.multiselect(
    'Select Gender:',
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)

# Filter by Company Type
company_filter = st.sidebar.multiselect(
    'Select Company Type:',
    options=df['Company Type'].unique(),
    default=df['Company Type'].unique()
)


# Visualization: Burn Rate by Designation
st.subheader('Burn Rate by Designation')
burn_rate_by_designation = filtered_data.groupby('Designation')['Burn Rate'].mean()
st.bar_chart(burn_rate_by_designation)




# Visualization: Designation by Resource Allocation
st.subheader('Designation by Resource Allocation')
Designation_by_Resource_Allocation = filtered_data.groupby('Resource Allocation')['Designation'].mean()
st.bar_chart(Designation_by_Resource_Allocation)




# Calculate average Burn Rate and Resource Allocation by Season
avg_burn_rate_by_season = df.groupby('Season')['Burn Rate'].mean()
avg_resource_allocation_by_season = df.groupby('Season')['Resource Allocation'].mean()



# Plotting the line plots side by side
fig, ax = plt.subplots(1, 2, figsize=(18, 9))

# Line plot for Burn Rate by Season
ax[0].plot(avg_burn_rate_by_season.index, avg_burn_rate_by_season.values, marker='o', linestyle='-')
ax[0].set_title('Average Burn Rate by Season')
ax[0].set_xlabel('Season')
ax[0].set_ylabel('Average Burn Rate')
ax[0].grid(True)

# Line plot for Resource Allocation by Season
ax[1].plot(avg_resource_allocation_by_season.index, avg_resource_allocation_by_season.values, marker='o', linestyle='-')
ax[1].set_title('Average Resource Allocation by Season')
ax[1].set_xlabel('Season')
ax[1].set_ylabel('Average Resource Allocation')
ax[1].grid(True)

st.pyplot(fig)




# Visualization: Average Resource Allocation by Company Type
st.subheader('Average Resource Allocation by Company Type')
resource_allocation_by_company = filtered_data.groupby('Company Type')['Resource Allocation'].mean()
st.bar_chart(resource_allocation_by_company)

 

 



# Pie charts for Male and Female distribution
st.subheader('Gender Destribution')

# Data for pie charts
male_data = filtered_data[filtered_data['Gender'] == 'Male']
female_data = filtered_data[filtered_data['Gender'] == 'Female']

# Create columns for side-by-side charts
col1, col2 = st.columns(2)

with col1:
    st.subheader('Male Employees Destribution')
    fig1, ax1 = plt.subplots()
    ax1.pie(male_data['Company Type'].value_counts(), labels=male_data['Company Type'].value_counts().index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

with col2:
    st.subheader('Female Employees Destribution')
    fig2, ax2 = plt.subplots()
    ax2.pie(female_data['Company Type'].value_counts(), labels=female_data['Company Type'].value_counts().index, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig2)




# 
st.write("# Burn out Rate")

# Create the bar plot with Seaborn
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x="Gender", y="Burn Rate",hue= "Company Type", ci="sd", ax=ax1)

# Set the y-axis label
ax1.set_ylabel("Burn out rate")

# Show the plot
st.pyplot(fig1)




fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x="WFH Setup Available", y="Burn Rate", data=df, ax=ax2)
ax2.set_xlabel('WFH Setup Available')
ax2.set_ylabel('Burn Rate')
ax2.set_title('Burn Rate by WFH Setup and Gender')
st.pyplot(fig2)



# Display some statistics
st.subheader('Statistics')
st.write(filtered_data.describe())

# Create dummy variables for 'Gender' and 'WFH Setup Available'
df = pd.get_dummies(df, columns=["Gender", "WFH Setup Available"], dtype=int)

# Reset the DataFrame index
df = df.reset_index(drop=True)

# Create a heat map of the correlations
st.header("Heat Map of Correlations")

# Calculate the correlation matrix for specified columns
cols = ['Designation', 'Resource Allocation', 'Mental Fatigue Score', 'Burn Rate', 'Gender_Male', 'Gender_Female']
correlation_matrix = df[cols].corr()

# Plot the heat map
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', ax=ax)
ax.set_title('Correlation Heat Map')
st.pyplot(fig)






























#### 3D PLOT
## Gender = 'Female' bo'lgan ma'lumotlarni filtrlaymiz
#female_data = df[df['Gender'] == 'Female']
#
## 3D plot chizish
#fig = plt.figure(figsize=(10, 7))
#ax = fig.add_subplot(111, projection='3d')
#
## X, Y, Z o'qlari
#x = female_data['Designation']
#y = female_data['Mental Fatigue Score']
#z = female_data['Burn Rate']
#
#ax.scatter(x, y, z, c='r', marker='o')
#
#ax.set_xlabel('Designation')
#ax.set_ylabel('Mental Fatigue Score')
#ax.set_zlabel('Burn Rate')
#
#st.pyplot(fig)
