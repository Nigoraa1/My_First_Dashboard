import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from streamlit_image_select import image_select
import yfinance as yf
import streamlit as st
import io


df = pd.read_csv("main_.csv")

st.write("# Burning out 🧠🤯")


# sidebarga rasm joylashtirish
st.sidebar.image('https://infographicjournal.com/wp-content/uploads/2021/10/remote-work-burnout.jpg',use_column_width=True)






# datasetning maqsadi haqida qisqacha ma'lumot
st.text("""Globally, World Mental Health Day is celebrated on October 10 each year. 
        The objective of this day is to raise awareness about mental health issues around 
        the world and mobilize efforts in support of mental health. According to an anonymous 
        survey, about 450 million people live with mental disorders that can be one of the primary 
        causes of poor health and disability worldwide. These days when the world is suffering from a 
        pandemic situation, it becomes really hard to maintain mental fitness.""")




# datasetni streamlit orqali ko'rish
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


# Filling MIssing Datas

st.write("# _____________________PART ONE___________________     ")
st.write("# ________________Filling Missing Datas________________ #")


st.write("Resource Allocation Column")

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

# Display the plots side by side using Streamlit
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


























# Ayol va erkaklarni Burn Rate umumiy bar charda korsatish
st.write("# Burn out Rate")
men = df[df["Gender"] == "Male"]
women = df[df["Gender"] == "Female"]


fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar("Male",
        men["Burn Rate"].mean(),
        yerr=men["Burn Rate"].std())
ax1.bar("Female",
        women["Burn Rate"].mean(),
        yerr=women["Burn Rate"].std())
ax1.set_ylabel("Burn out rate")
st.pyplot(fig1)




fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x="WFH Setup Available", y="Burn Rate", data=df, hue="Gender", ax=ax2)
ax2.set_xlabel('WFH Setup Available')
ax2.set_ylabel('Burn Rate')
ax2.set_title('Burn Rate by WFH Setup and Gender')
st.pyplot(fig2)





# 'WFH Setup Available' 'Yes' bo'lganda filtrlash
filtered_data = df[df['WFH Setup Available'] == 'Yes']

# Erkaklar va ayollar uchun alohida barplot yaratish
male_data = filtered_data[filtered_data['Gender'] == 'Male']
female_data = filtered_data[filtered_data['Gender'] == 'Female']





# Streamlit konfiguratsiyasi
st.title("Burn Rate Analysis by Gender")
st.write("Comparing Burn Rate between Male and Female")

# Burn Rate ni chizish
fig, ax = plt.subplots(figsize=(10, 6))

ax.hist(male_data['Burn Rate'], bins=20, alpha=0.5, label='Male')
ax.hist(female_data['Burn Rate'], bins=20, alpha=0.5, label='Female')

ax.set_xlabel('Burn Rate')
ax.set_ylabel('Frequency')
ax.set_title('Burn Rate DFrequency')
ax.legend()

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


