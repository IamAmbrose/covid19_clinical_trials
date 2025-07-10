# app.py
# 📊 COVID-19 Clinical Trials Dashboard with Streamlit

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Page setup ---
st.set_page_config(page_title="COVID-19 Clinical Trials Dashboard", layout="wide")

# --- Title ---
st.title("🧬 COVID-19 Clinical Trials Dashboard")

st.markdown(
    """
    Explore COVID-19 clinical trials worldwide — filter by country, status, phase and see trends, distributions, and key insights.
    """
)

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_covid_clinical_trials.csv")
    df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
    df['Year'] = df['Start Date'].dt.year
    df['Month'] = df['Start Date'].dt.month
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filters")

country_options = df['Country'].dropna().unique()
selected_countries = st.sidebar.multiselect(
    "Select Country(s):",
    options=country_options,
    default=df['Country'].value_counts().head(5).index.tolist()
)

status_options = df['Status'].dropna().unique()
selected_status = st.sidebar.multiselect(
    "Select Trial Status:",
    options=status_options,
    default=status_options
)

phase_options = df['Phases'].dropna().unique()
selected_phases = st.sidebar.multiselect(
    "Select Trial Phases:",
    options=phase_options,
    default=phase_options
)

# --- Filter Data ---
filtered_df = df[
    (df['Country'].isin(selected_countries)) &
    (df['Status'].isin(selected_status)) &
    (df['Phases'].isin(selected_phases))
]

# --- KPI Metrics ---
st.subheader("📌 Key Figures")
col1, col2, col3 = st.columns(3)

col1.metric("Total Trials", f"{len(filtered_df):,}")
col2.metric("Unique Countries", filtered_df['Country'].nunique())
col3.metric("Unique Sponsors", filtered_df['Sponsor/Collaborators'].nunique())

st.markdown("---")

# --- Visualizations ---
# 1. Status Distribution
st.subheader("📊 Status Distribution")
fig1, ax1 = plt.subplots(figsize=(8,5))
sns.countplot(data=filtered_df, y='Status', order=filtered_df['Status'].value_counts().index, ax=ax1)
ax1.set_xlabel("Count")
st.pyplot(fig1)

# 2. Phases Distribution
st.subheader("📊 Phases Distribution")
fig2, ax2 = plt.subplots(figsize=(8,5))
sns.countplot(data=filtered_df, y='Phases', order=filtered_df['Phases'].value_counts().index, ax=ax2)
ax2.set_xlabel("Count")
st.pyplot(fig2)

# 3. Top 10 Countries
st.subheader("🌍 Top 10 Countries by Trial Count")
fig3, ax3 = plt.subplots(figsize=(8,5))
filtered_df['Country'].value_counts().head(10).plot(kind='barh', ax=ax3)
ax3.set_xlabel("Number of Trials")
ax3.set_ylabel("Country")
st.pyplot(fig3)

# 4. Trials Over Time
st.subheader("📈 Trials Started Over Time")
fig4, ax4 = plt.subplots(figsize=(10,5))
filtered_df.groupby('Year').size().plot(kind='bar', ax=ax4)
ax4.set_ylabel("Number of Trials")
ax4.set_xlabel("Year")
st.pyplot(fig4)

# 5. Age Group Distribution
st.subheader("👥 Age Group Distribution")
fig5, ax5 = plt.subplots(figsize=(8,5))
filtered_df['Age'].value_counts().plot(kind='bar', ax=ax5)
ax5.set_xlabel("Age Group")
ax5.set_ylabel("Number of Trials")
st.pyplot(fig5)

# 6. Start Month Trend
st.subheader("📆 Start Month Distribution")
fig6, ax6 = plt.subplots(figsize=(10,5))
filtered_df['Month'].dropna().value_counts().sort_index().plot(kind='bar', ax=ax6)
ax6.set_xlabel("Start Month")
ax6.set_ylabel("Number of Trials")
ax6.set_xticks(range(12))
ax6.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], rotation=45)
st.pyplot(fig6)

st.success("✅ Dashboard Ready — explore the data and adjust filters!")
