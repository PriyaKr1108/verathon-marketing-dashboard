import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import os

# Page configuration
st.set_page_config(
    page_title="Verathon Marketing Platform",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #0056A7;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #333333;
    }
    .description {
        font-size: 1.1rem;
        color: #555555;
    }
    .highlight {
        background-color: #f0f7ff;
        padding: 20px;
        border-radius: 5px;
        border-left: 5px solid #0056A7;
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown('<div class="main-header">Verathon Marketing Intelligence Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Powered by Digital Factory 24</div>', unsafe_allow_html=True)

# Main content columns
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="description">Welcome to the comprehensive marketing intelligence platform designed specifically for Verathon. This platform integrates digital marketing analytics, webinar management, competitive intelligence, and more to provide actionable insights for your marketing campaigns.</div>', unsafe_allow_html=True)
    
    st.markdown("### Digital Marketing Growth Maturity Framework")
    st.markdown("""
    The Digital Factory 24 Growth Maturity Framework helps organizations assess their current marketing capabilities and develop a roadmap for improvement:
    
    1. **Crawl Stage**: Establishing fundamentals and basic analytics
    2. **Walk Stage**: Implementing automation and personalization
    3. **Run Stage**: Advanced analytics and AI-driven optimization
    """)
    
    # Create sample maturity data
    maturity_categories = ['Website Optimization', 'Email Marketing', 'Content Strategy', 'Social Media', 'Analytics', 'Automation']
    maturity_levels = {
        'Current': [1, 2, 1, 2, 1, 0],
        'Target': [2, 3, 2, 3, 2, 2],
    }
    
    # Create radar chart
    fig = go.Figure()
    
    # Add traces for current and target
    fig.add_trace(go.Scatterpolar(
        r=maturity_levels['Current'],
        theta=maturity_categories,
        fill='toself',
        name='Current State'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=maturity_levels['Target'],
        theta=maturity_categories,
        fill='toself',
        name='Target State'
    ))
    
    # Update layout
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 3]
            )
        ),
        showlegend=True,
        height=400,
        margin=dict(l=70, r=70, t=20, b=70),
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<div class="highlight">Navigate to specific modules using the sidebar to explore detailed analytics and tools for each marketing function.</div>', unsafe_allow_html=True)

with col2:
    st.markdown("### Recent KPI Overview")
    
    # Sample KPIs
    kpis = {
        "Marketing Qualified Leads": {"value": 128, "change": 12.4, "unit": "%"},
        "Webinar Registrations": {"value": 342, "change": 8.7, "unit": "%"},
        "Website Conversion Rate": {"value": 3.24, "change": 0.6, "unit": "pp"},
        "Social Media Engagement": {"value": 9876, "change": -2.3, "unit": "%"}
    }
    
    # Display KPIs
    for kpi_name, kpi_data in kpis.items():
        st.metric(
            label=kpi_name,
            value=kpi_data["value"] if "pp" not in kpi_data["unit"] else f"{kpi_data['value']}%",
            delta=f"{kpi_data['change']}{kpi_data['unit']}"
        )
    
    st.markdown("### Upcoming Webinars")
    st.info("Medical Device Innovations - May 15")
    st.info("Healthcare Marketing Trends - June 2")
    
# Footer
st.markdown("---")
st.markdown("© 2024 Digital Factory 24 | All Rights Reserved")
