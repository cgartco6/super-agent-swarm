import streamlit as st
import sys
import os

# Fix import path for Streamlit Cloud
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from swarm.swarm_orchestrator import create_swarm
    from utils.logger import get_logger
    IMPORT_SUCCESS = True
except ImportError as e:
    IMPORT_SUCCESS = False
    st.error(f"Import Error: {e}")

import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="Super Agent Swarm", layout="wide")

st.title("🚀 Super Agent Swarm Command Center")
st.markdown("### Advanced Multi-Agent Orchestration Dashboard")

if not IMPORT_SUCCESS:
    st.warning("Some modules are missing. Please check your GitHub repository structure.")
    st.stop()

logger = get_logger("CommandCenter")

# Sidebar
with st.sidebar:
    st.header("⚙️ Control Panel")
    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key

# Rest of your UI code (tabs, etc.)
tab1, tab2, tab3 = st.tabs(["🎯 Orchestrate", "📊 Monitoring", "🧩 Modules"])

with tab1:
    st.subheader("Launch Swarm Mission")
    goal = st.text_area("Enter your goal", height=120, 
                       placeholder="Build a marketing campaign...")
    
    if st.button("🚀 Launch Swarm", type="primary"):
        with st.spinner("Swarm is working..."):
            try:
                swarm = create_swarm()
                result = swarm.process(goal)
                st.success("Done!")
                st.write(result)
            except Exception as e:
                st.error(f"Error: {e}")

st.caption("If you still see loading issues, check that all folders (agents/, swarm/, tools/, utils/) are pushed to GitHub.")
