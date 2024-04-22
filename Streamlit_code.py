import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
@st.cache
def load_data():
    return pd.read_csv('cancer patient data sets')

data = load_data()

# Set up your Streamlit app
st.title('Cancer Patient Data Analysis')
st.write("This app displays the histograms for Air Pollution, Alcohol use, Smoking, and Occupational Hazards.")

# Display histograms for the selected features
fig, ax = plt.subplots(2, 2, figsize=(10, 10))

ax[0, 0].hist(data['Air Pollution'], bins=10, color='skyblue')
ax[0, 0].set_title('Air Pollution')

ax[0, 1].hist(data['Alcohol use'], bins=10, color='lightgreen')
ax[0, 1].set_title('Alcohol use')

ax[1, 0].hist(data['Smoking'], bins=10, color='salmon')
ax[1, 0].set_title('Smoking')

ax[1, 1].hist(data['OccuPational Hazards'], bins=10, color='orange')
ax[1, 1].set_title('Occupational Hazards')

# Adjust layout
plt.tight_layout()
st.pyplot(fig)
