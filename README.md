# 📊 COVID-19 Clinical Trials Dashboard

An **interactive dashboard** built with **Streamlit** to explore COVID-19 clinical trials worldwide using open data from ClinicalTrials.gov.

---

## 🎯 **Project Objective**

The goal of this project is to perform **Exploratory Data Analysis (EDA)** on COVID-19 clinical trials data to:
- Understand how clinical research responded during the pandemic
- Analyze key characteristics such as **status**, **phases**, **demographics**, **sponsors**, and **geographic trends**
- Provide clear, interactive insights for researchers, public health agencies, and the public
- Offer a ready-to-use dashboard for continuous exploration

---

## ✅ **Key Findings**

- The **majority of trials** were in **Phase II and Phase III**, focusing on treatment efficacy and safety in larger populations.
- **USA, France, UK, and Italy** contributed the highest number of trials.
- Most studies targeted **adult populations** — fewer studies were focused on pediatric groups.
- The **peak in trial starts** occurred during **2020 and 2021**, showing an intense global research response.
- Status breakdown revealed most trials are **Completed**, **Recruiting**, or **Active**, reflecting ongoing COVID-19 research efforts.

---

## 📌 **Features**

✔️ Dynamic sidebar filters (Country, Phase, Status)  
✔️ Visuals: Status, Phases, Age Groups, Top Countries  
✔️ Yearly and monthly trends  
✔️ KPIs: Total trials, unique countries, unique sponsors  
✔️ Fully interactive — run locally or in the cloud

---

## 🚀 **Live Dashboard**

🔗 **[👉 Open the Live Dashboard](https://covid19clinicaltrials-aycfu6kkcmzgnqk6yosayx.streamlit.app/)**

---

## 🗂️ **Project Files**

- `app.py` — Streamlit application script
- `cleaned_covid_clinical_trials.csv` — Cleaned dataset
- `requirements.txt` — Python dependencies

---

## ⚙️ **How to Run Locally**

```bash
# 1. Clone this repo
git clone https://github.com/YOUR_USERNAME/covid19-trials-dashboard.git
cd covid19-trials-dashboard

# 2. Install requirements
pip install -r requirements.txt

# 3. Run Streamlit app
streamlit run app.py
