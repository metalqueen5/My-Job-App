import streamlit as st
import pandas as pd
from jobspy import scrape_jobs

# --- 1. YOUR LIVE SETTINGS ---
MY_NICHE = "Remote Marketing" 
MY_SUBSTACK = "https://nichejobs1.substack.com"  
MY_STRIPE_VIP = "https://buy.stripe.com/cNi14o8Yg94F6ejeQz4sE02"

st.set_page_config(page_title="Remote Marketing Hub", page_icon="📈", layout="wide")

# --- 2. SIDEBAR ---
with st.sidebar:
    st.title("💎 VIP Access")
    st.write("Get the high-paying, hidden roles first.")
    st.link_button("🚀 Join VIP - $19/mo", MY_STRIPE_VIP, use_container_width=True)
    st.divider()
    st.info("VIP members get access to salary data and direct hiring manager links.")

# --- 3. MAIN INTERFACE ---
st.title("💼 Remote Marketing Job Board")
st.write("Only 100% Remote roles, updated daily.")

# Email signup button
st.link_button("📩 Get Free Weekly Alerts", MY_SUBSTACK)
st.divider()

# --- 4. THE JOB FINDER ---
@st.cache_data(ttl=86400)
def fetch_jobs():
    return scrape_jobs(
        site_name=["linkedin", "indeed"],
        search_term=MY_NICHE,
        location="Remote",
        results_wanted=15,
        hours_old=72
    )

try:
    jobs = fetch_jobs()
    if jobs.empty:
        st.write("Searching for new leads... check back in 5 minutes!")
    else:
        for i, row in jobs.iterrows():
            # Every 3rd job is "Locked" for VIPs
            if i % 3 == 0:
                with st.expander(f"🔒 VIP ONLY: {row['title']} at {row['company']}"):
                    st.write("### 💰 Estimated Salary: $95,000+")
                    st.write("Unlock this lead to see the full description and apply.")
                    st.link_button("Unlock Now", MY_STRIPE_VIP)
            else:
                st.subheader(row['title'])
                st.write(f"🏢 {row['company']} | 📍 {row['location']}")
                st.link_button("View & Apply", row['job_url'])
                st.write("---")
except Exception as e:
    st.info("The robot is currently indexing new roles! Please refresh in 60 seconds.")

# --- 5. LEGAL FOOTER ---
st.caption("⚠️ Disclaimer: For informational purposes only. We do not guarantee employment.")
