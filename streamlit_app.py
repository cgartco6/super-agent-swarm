import streamlit as st
import sys
import os

# Adjust path for cloud deployment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from swarm.swarm_orchestrator import create_swarm
from utils.logger import get_logger
import pandas as pd
import plotly.express as px
from datetime import datetime

logger = get_logger("CommandCenter")

st.set_page_config(page_title="Super Agent Swarm", layout="wide")

st.title("🚀 Super Agent Swarm Command Center")
st.markdown("### Advanced Multi-Agent Orchestration Dashboard")

# [Rest of the code remains exactly the same as I gave you earlier]

# ... (copy the full code from my previous message here)
