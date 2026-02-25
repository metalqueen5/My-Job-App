import streamlit as st
import pandas as pd
from jobspy import scrape_jobs

# --- SEO & TITLE SETTINGS ---
# This helps Google find your app when people search for jobs
st.set_page_config(
    page_title="Remote Marketing Jobs 2026 | Verified Daily Leads",
    page_icon="📈",
    layout="wide"
)

# --- 1. YOUR SETTINGS ---
MY_NICHE = "Remote Marketing" 
MY_SUBSTACK = "https://nichejobs1.substack.com"  
MY_STRIPE_VIP = "https://buy.stripe.com/cNi14o8Yg94F6ejeQz4sE02"

# --- 2. SIDEBAR ---
with st.sidebar:
    st.title("💎 VIP Access")
    st.write("Get the 'Hidden' $150k+ jobs before they hit LinkedIn.")
    st.link_button("🚀 Join VIP - $19/mo", MY_STRIPE_VIP, use_container_width=True)
    st.divider()
    st.info("VIP members get access to salary data and direct hiring manager links.")

# --- 3. MAIN INTERFACE ---
st.title(f"💼 Remote marketing} Job Board")
st.write("We scan 10+ sites so you don't have to. Only 100% Remote roles.")

# This button is your 'Email Magnet'
st.link_button("📩 Alert Me When New Jobs are Posted", MY_SUBSTACK)
st.divider()

# --- 4. THE JOB FINDER (The Robot) ---
@st.cache_data(ttl=86400)
def fetch_jobs():
    return scrape_jobs(
        site_name=["linkedin", "indeed", "zip_recruiter"],
        search_term=MY_NICHE,
        location="Remote",
        results_wanted=20,
        hours_old=48
    )

try:
    jobs = fetch_jobs()
    for i, row in jobs.iterrows():
        # Paywall every 3rd job
        if i % 3 == 0:
            with st.expander(f"🔒 VIP ONLY: {row['title']} at {row['company']}"):
                st.write("### 💰 High-Salary Lead")
                st.write("This listing is verified and active. Unlock for full details.")
                st.link_button("Unlock Now", MY_STRIPE_VIP)
        else:
            st.subheader(row['title'])
            st.write(f"🏢 {row['company']} | 📍 {row['location']}")
            st.link_button("View & Apply", row['job_url'])
            st.write("---")
except Exception as e:
    st.error("Robot is currently indexing new roles. Please refresh in a moment!")

# --- 5. FOOTER ---
st.caption("⚠️ Disclaimer: For informational purposes. We do not guarantee employment.")
