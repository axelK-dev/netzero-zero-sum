import streamlit as st
import pandas as pd

# ---------------------------
# Global Settings
# ---------------------------
st.set_page_config(page_title="Net Zero – Zero Sum", layout="wide")

# Sidebar Navigation
st.sidebar.title("🌍 Global Oversight")
page = st.sidebar.radio("Navigate", ["Overview", "Economy", "Politics", "Culture", "Security", "Climate", "News Feed"])

# ---------------------------
# Page: Overview
# ---------------------------
if page == "Overview":
    st.title("🌐 Net Zero – Zero Sum Dashboard")
    st.subheader("Global Status at a Glance")

    # Placeholder for global KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Global GDP", "$100T", "+2%")
    col2.metric("Temperature Rise", "1.2°C", "+0.01°C")
    col3.metric("Carbon Price", "$50", "+$5")

    st.markdown("---")
    st.write("### World Map (Placeholder)")
    st.map(pd.DataFrame({"lat": [37.76], "lon": [-122.4]}))  # Example map

# ---------------------------
# Page: Economy
# ---------------------------
elif page == "Economy":
    st.title("💰 Economy Module")
    st.write("Track GDP, carbon pricing, subsidies, and trade.")
    st.line_chart(pd.DataFrame({"GDP": [100, 102, 104], "Carbon Price": [50, 55, 60]}))

# ---------------------------
# Page: Politics
# ---------------------------
elif page == "Politics":
    st.title("🏛 Politics Module")
    st.write("Policy adoption, treaties, lobbying.")
    st.progress(70)  # Example: policy adoption progress

# ---------------------------
# Page: Culture
# ---------------------------
elif page == "Culture":
    st.title("🎭 Culture Module")
    st.write("Public opinion, activism, misinformation.")
    st.bar_chart(pd.DataFrame({"Public Opinion": [0.6, 0.62, 0.65]}))

# ---------------------------
# Page: Security
# ---------------------------
elif page == "Security":
    st.title("🛡 Security Module")
    st.write("Resource conflicts, migration, cyber threats.")
    st.metric("Conflict Risk", "10%", "-0.5%")

# ---------------------------
# Page: Climate
# ---------------------------
elif page == "Climate":
    st.title("🌱 Climate Module")
    st.write("Emissions, temperature rise, tipping points.")
    st.line_chart(pd.DataFrame({"Emissions": [40, 39.8, 39.5], "Temperature": [1.1, 1.12, 1.13]}))

# ---------------------------
# Page: News Feed
# ---------------------------
elif page == "News Feed":
    st.title("📰 Global News & OSINT Updates")
    st.write("Simulated social-media style feed for realism.")
    st.markdown("""
    **Breaking:** New climate treaty signed by major economies.
    *Source: UN Data*
    ---
    **Alert:** Arctic ice melt accelerates beyond projections.
    *Source: NASA Climate*
    """)