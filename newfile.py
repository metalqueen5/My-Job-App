import streamlit as st
import pandas as pd
from jobspy import scrape_jobs

# --- PASTE YOUR LINKS HERE ---
MY_NICHE = "Remote Marketing" 
MY_SUBSTACK = "https://nichejobs1.substack.com/?r=7npwbk&utm_campaign=pub-share-checklist"
MY_STRIPE = "https://buy.stripe.com/test_5kQdRa8YgbcN9qvbEn4sE00"

st.set_page_config(page_title="Job Board", page_icon="🚀")

# 1. THE HEADER
st.title(f"💼 {MY_NICHE} Job Board")
st.write("Automatically updated every 24 hours.")

# 2. THE ACTION BUTTONS
col1, col2 = st.columns(2)
with col1:
    st.link_button("📩 Get Email Alerts", MY_SUBSTACK, use_container_width=True)
with col2:
    st.link_button("🌟 Feature a Job ($49)", MY_STRIPE, use_container_width=True)

st.divider()

# 3. THE AUTOMATED JOB FINDER
@st.cache_data(ttl=86400) # This saves data for 24 hours so it's lightning fast
def fetch_jobs():
    return scrape_jobs(
        site_name=["indeed", "linkedin"],
        search_term=MY_NICHE,
        location="USA",
        results_wanted=10,
        hours_old=72
    )

try:
    jobs = fetch_jobs()
    for _, row in jobs.iterrows():
        with st.container():
            st.subheader(row['title'])
            st.write(f"🏢 {row['company']} | 📍 {row['location']}")
            st.link_button("View Job", row['job_url'])
            st.write("---")
except:
    st.info("I'm updating the job list right now! Please refresh in 60 seconds.")st.divider()
st.caption("⚠️ Disclaimer: This job board is for informational purposes. While we strive for accuracy, we do not guarantee employment or verify every employer. Use at your own risk.")

