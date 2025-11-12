import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(layout="wide")

# --- Dashboard Title ---
st.title("The AI & Employment Monitor")
st.markdown("A dashboard tracking AI's impact on jobs, skills, and wages.")

st.divider()

# --- 1. Executive Summary (KPIs) ---
st.header("📈 Executive Summary")
st.markdown("High-level global metrics from key 2024/2025 reports.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        label="Net Job Impact (WEF 2025 Proj.)",
        value="+12 Million",
        delta="97M New Roles vs. 85M Displaced",
        delta_color="normal"
    )
with col2:
    st.metric(
        label="AI Skill Wage Premium (PwC 2025)",
        value="+56%",
        delta="Avg. wage premium for AI-skilled jobs",
        delta_color="normal"
    )
with col3:
    st.metric(
        label="AI-Exposed Wage Growth (PwC 2025)",
        value="2x Faster",
        delta="vs. non-exposed industries",
        delta_color="normal"
    )

st.divider()

# --- 2. Job Transformation vs. Creation ---
col_risk, col_growth = st.columns(2)

with col_risk:
    st.subheader("⚠️ Job Transformation: Roles at Risk")
    st.markdown("Top roles by automation potential (Source: Goldman Sachs, WEF)")
    # Static data for roles at risk
    data_risk = pd.DataFrame({
        'Job Title': ['Data Entry Clerks', 'Customer Service Reps', 'Administrative Secretaries', 'Accountants & Bookkeepers', 'Paralegals'],
        'Automation Potential (%)': [85, 78, 75, 72, 69]
    })
    fig_risk = px.bar(
        data_risk.sort_values(by="Automation Potential (%)", ascending=True),
        x='Automation Potential (%)', y='Job Title', orientation='h',
        title="Top Roles by Automation Potential",
        color='Automation Potential (%)', color_continuous_scale=px.colors.sequential.Reds
    )
    st.plotly_chart(fig_risk, use_container_width=True)

with col_growth:
    st.subheader("🚀 Job Creation: New & Growing Roles")
    st.markdown("Fastest-growing roles in the AI economy (Source: WEF, PwC)")
    # Static data for growing roles
    data_growth = pd.DataFrame({
        'Job Title': ['AI/ML Specialist', 'Data Scientist', 'Big Data Specialist', 'AI Product Manager', 'Prompt Engineer'],
        'Projected Growth (%)': [45, 38, 35, 31, 28]
    })
    fig_growth = px.bar(
        data_growth.sort_values(by="Projected Growth (%)", ascending=False),
        x='Job Title', y='Projected Growth (%)',
        title="Fastest-Growing AI-Related Jobs",
        color='Projected Growth (%)', color_continuous_scale=px.colors.sequential.Greens
    )
    st.plotly_chart(fig_growth, use_container_width=True)

st.divider()

# --- 3. Canada Focus (STATIC DATA) ---
st.header("🇨🇦 Canada Focus: The Local Impact")
st.markdown("Data from Statistics Canada (Q3 2025 Report). *Live data feed is temporarily offline pending Q4 data release.*")

col_can1, col_can2 = st.columns(2)

with col_can1:
    st.subheader("Expected AI Hiring Impact (Next 12 Mos)")
    
    # Using the last known data from the Q3 report
    st.metric(
        label="Businesses Expecting an *Increase* in Jobs",
        value="10.8%", # Static value
        delta="Q3 2025 Expectations"
    )
    st.metric(
        label="Businesses Expecting *No Change* in Jobs",
        value="77.2%", # Static value
        delta="Q3 2025 Expectations"
    )
    st.metric(
        label="Businesses Expecting a *Decrease* in Jobs",
        value="12.0%", # Static value
        delta="Q3 2025 Expectations",
        delta_color="inverse"
    )

with col_can2:
    st.subheader("Top Sectors *Planning to Hire AI Staff* (Next 12 Mos)")
    
    # Using the last known data from the Q3 report
    industry_data = pd.DataFrame({
        "Industry": [
            "Information and cultural industries",
            "Professional, scientific and technical services",
            "Finance and insurance"
        ],
        "Planning to Hire AI Staff (%)": [21.4, 20.9, 15.1] # Static values
    })

    st.dataframe(
        industry_data,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Industry": st.column_config.Column("Industry Sector", width="large"),
            "Planning to Hire AI Staff (%)": st.column_config.ProgressColumn(
                "Planning to Hire AI Staff",
                format="%.1f%%",
                min_value=0,   # <-- THE FIX
                max_value=100, # <-- THE FIX
            ),
        }
    )

st.divider()
st.caption("Dashboard by VisiVault Analytics | Data Sources: WEF, PwC, Goldman Sachs, Statistics Canada")
