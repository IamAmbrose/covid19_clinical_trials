# COVID-19 Clinical Trials Dashboard

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title=\"COVID-19 Trials Dashboard\", layout=\"wide\")

# === 1. Title ===
st.title(\"COVID-19 Clinical Trials Dashboard\")

# === 2. Load Data ===
@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_covid_clinical_trials.csv')
    df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
    df['Year'] = df['Start Date'].dt.year
    df['Month'] = df['Start Date'].dt.month
    return df

df = load_data()

# === 3. Sidebar Filters ===
st.sidebar.header(\"Filters\")

countries = st.sidebar.multiselect(
    \"Select Countries:\", 
    options=df['Country'].dropna().unique(),
    default=df['Country'].value_counts().head(5).index.tolist()
)

status = st.sidebar.multiselect(
    \"Select Trial Status:\",
    options=df['Status'].dropna().unique(),
    default=df['Status'].unique()
)

phases = st.sidebar.multiselect(
    \"Select Trial Phases:\",
    options=df['Phases'].dropna().unique(),
    default=df['Phases'].unique()
)

# Filter Data
df_filtered = df[
    (df['Country'].isin(countries)) &
    (df['Status'].isin(status)) &
    (df['Phases'].isin(phases))
]

# === 4. KPI Metrics ===
st.subheader(\"Key Figures\")
col1, col2, col3 = st.columns(3)

col1.metric(\"Total Trials\", f\"{len(df_filtered):,}\")
col2.metric(\"Unique Countries\", df_filtered['Country'].nunique())
col3.metric(\"Unique Sponsors\", df_filtered['Sponsor/Collaborators'].nunique())

# === 5. Plots ===

st.subheader(\"Status Distribution\")
fig1, ax1 = plt.subplots()
sns.countplot(y='Status', data=df_filtered, order=df_filtered['Status'].value_counts().index, ax=ax1)
st.pyplot(fig1)

st.subheader(\"Phases Distribution\")
fig2, ax2 = plt.subplots()
sns.countplot(y='Phases', data=df_filtered, order=df_filtered['Phases'].value_counts().index, ax=ax2)
st.pyplot(fig2)

st.subheader(\"Top Countries\")
fig3, ax3 = plt.subplots()
df_filtered['Country'].value_counts().head(10).plot(kind='barh', ax=ax3)
ax3.set_xlabel(\"Number of Trials\")
st.pyplot(fig3)

st.subheader(\"Trials Over Time\")
fig4, ax4 = plt.subplots()
df_filtered.groupby('Year').size().plot(kind='bar', ax=ax4)
ax4.set_ylabel(\"Number of Trials\")
st.pyplot(fig4)

st.subheader(\"Age Group Distribution\")
fig5, ax5 = plt.subplots()
df_filtered['Age'].value_counts().plot(kind='bar', ax=ax5)
ax5.set_xlabel(\"Age Group\")
ax5.set_ylabel(\"Number of Trials\")
st.pyplot(fig5)

st.success(\"✅ Dashboard Loaded Successfully!\")
