import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from swarm.swarm_orchestrator import create_swarm
from utils.logger import get_logger
import pandas as pd
import plotly.express as px
from datetime import datetime

logger = get_logger("CommandCenter")

# Page config
st.set_page_config(
    page_title="Super Agent Swarm Command Center",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🚀 Super Agent Swarm Command Center")
st.markdown("### Advanced Multi-Agent Orchestration Dashboard & Command Centre")

# Sidebar
with st.sidebar:
    st.header("⚙️ Control Panel")
    
    api_key = st.text_input("OpenAI API Key", type="password", 
                           value=os.getenv("OPENAI_API_KEY", ""))
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        st.success("API Key set", icon="✅")
    
    st.divider()
    
    module = st.selectbox(
        "Select Active Module",
        ["Core Swarm", "Marketing Engine", "Custom Module"]
    )
    
    st.divider()
    st.markdown("**Add New Module**")
    new_module_name = st.text_input("Module Name")
    new_module_desc = st.text_area("Description & Goals", height=100)
    if st.button("Add Module"):
        st.success(f"Module '{new_module_name}' registered! Extend in code for full functionality.")
        st.info("Tip: Create new agent classes and update orchestrator.")

# Main Tabs
tab1, tab2, tab3 = st.tabs(["🎯 Orchestrate Mission", "📊 Monitoring", "🧩 Modules"])

with tab1:
    st.subheader("Launch Super Agent Swarm")
    goal = st.text_area(
        "Enter your mission goal", 
        height=150,
        placeholder="Create and execute an aggressive pure pull marketing campaign for a new AI productivity tool targeting freelancers..."
    )
    
    col1, col2 = st.columns(2)
    with col1:
        agent_count = st.slider("Swarm Size (Agents)", 3, 12, 5)
    with col2:
        temperature = st.slider("Creativity Level", 0.0, 1.0, 0.7)
    
    if st.button("🚀 LAUNCH SWARM", type="primary", use_container_width=True):
        if not goal.strip():
            st.error("Please enter a valid goal.")
        else:
            with st.spinner("Super Agent Swarm is planning, delegating, and executing..."):
                try:
                    swarm = create_swarm()
                    result = swarm.process(goal)
                    
                    st.success("✅ Mission Completed Successfully!")
                    st.markdown("### 📋 Final Output")
                    st.markdown(result)
                    
                    # Save to session history
                    if "history" not in st.session_state:
                        st.session_state.history = []
                    st.session_state.history.append({
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "goal": goal[:100] + "..." if len(goal) > 100 else goal,
                        "status": "Success",
                        "result_preview": result[:300] + "..." if len(result) > 300 else result
                    })
                except Exception as e:
                    st.error(f"❌ Error during execution: {str(e)}")

with tab2:
    st.subheader("Mission History & Analytics")
    if "history" in st.session_state and st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df, use_container_width=True)
        
        # Analytics chart
        fig = px.bar(
            df, 
            x="timestamp", 
            title="Missions Over Time",
            labels={"index": "Mission Count"}
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No missions launched yet. Start one in the Orchestrate tab!")

with tab3:
    st.subheader(f"Active Module: {module}")
    
    if module == "Marketing Engine":
        st.markdown("### 🔥 Advanced Aggressive Pure Pull Marketing Engine")
        st.caption("Configure criteria and launch a specialized swarm")
        
        col1, col2 = st.columns(2)
        with col1:
            target_audience = st.text_input("Target Audience", "Freelancers & solopreneurs")
            budget = st.number_input("Monthly Budget (USD)", min_value=500, value=2500)
        with col2:
            goals = st.multiselect(
                "Primary Goals", 
                ["Lead Generation", "Sales Conversion", "Brand Awareness", "Viral Growth", "Community Building"],
                default=["Lead Generation", "Sales Conversion"]
            )
        
        channels = st.multiselect("Key Channels", ["LinkedIn", "Twitter/X", "YouTube", "Blog/SEO", "Email", "TikTok"], default=["LinkedIn", "Blog/SEO"])
        content_strategy = st.text_area("Content Strategy & Pull Tactics", 
                                      "Value-first long-form content, case studies, free tools, community engagement...")
        
        if st.button("🚀 Launch Marketing Swarm", type="primary"):
            marketing_goal = f"""
            Execute an aggressive pure pull marketing campaign:
            Target: {target_audience}
            Goals: {goals}
            Budget: ${budget}
            Channels: {channels}
            Strategy: {content_strategy}
            """
            with st.spinner("Marketing Swarm executing..."):
                swarm = create_swarm()
                result = swarm.process(marketing_goal)
                st.success("Marketing Campaign Executed!")
                st.write(result)
    
    elif module == "Custom Module":
        st.info("Use the sidebar to add new modules. Then extend the agents/ folder.")
    else:
        st.info("Core Swarm ready. Use the Orchestrate tab to begin.")

st.caption("Super Agent Swarm Command Center • Built with Streamlit • Extend freely")
