import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

st.title("Bio Profile NER Analyzer")
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())

    profile = ProfileReport(df, title="Bio Profile Report", explorative=True)
    profile.to_file("streamlit_output.html")
    st.success("Profile generated! Download below.")

    with open("streamlit_output.html", "rb") as f:
        st.download_button("📥 Download HTML Report", f, "bio_profile_report.html")