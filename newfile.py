import streamlit as st
import pandas as pd
from jobspy import scrape_jobs

# 1. SETUP YOUR BUSINESS STUFF HERE
NICHE = "Remote Marketing"  # Change this to whatever you want to sell!
STRIPE_LINK = "PASTE_YOUR_STRIPE_LINK_HERE" # Put your link from Step 2 here

# 2. THE WEBSITE INTERFACE
st.title(f"🚀 {NICHE} Jobs")
st.sidebar.header("Employers")
st.sidebar.markdown(f"[🌟 Feature a Job ($49)]({STRIPE_LINK})")

# 3. THE AUTOMATIC JOB HUNTER
@st.cache_data(ttl=3600)
def get_jobs():
    return scrape_jobs(
        site_name=["indeed", "linkedin"],
        search_term=NICHE,
        location="USA",
        results_wanted=10
    )

# 4. SHOW THE JOBS
try:
    df = get_jobs()
    for _, row in df.iterrows():
        st.subheader(row['title'])
        st.write(f"{row['company']} | {row['location']}")
        st.link_button("View Job", row['job_url'])
        st.divider()
except:
    st.write("Refreshing jobs... check back in 1 minute!")
