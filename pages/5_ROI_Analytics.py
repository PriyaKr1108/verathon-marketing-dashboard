import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# Page configuration
st.set_page_config(
    page_title="ROI Analytics - Verathon",
    page_icon="💰",
    layout="wide"
)

# Header
st.title("Marketing ROI Analytics")
st.markdown("Track, analyze, and optimize your marketing investments")

# Date range selection
date_range = st.select_slider(
    "Select time period:",
    options=["Last 30 Days", "Last Quarter", "Last 6 Months", "Last Year", "YTD"],
    value="Last Quarter"
)

# ROI Overview
st.header("Marketing ROI Overview")
roi_cols = st.columns(4)

with roi_cols[0]:
    st.metric(
        label="Total Marketing Investment",
        value="$425,000",
        delta="$25,000",
        delta_color="inverse"
    )

with roi_cols[1]:
    st.metric(
        label="Attributed Revenue",
        value="$1,870,000",
        delta="$320,000"
    )

with roi_cols[2]:
    st.metric(
        label="Marketing ROI",
        value="4.4x",
        delta="0.5x"
    )

with roi_cols[3]:
    st.metric(
        label="Customer Acquisition Cost",
        value="$1,250",
        delta="-$120",
        delta_color="inverse"
    )

# ROI by Channel
st.header("ROI by Marketing Channel")
channel_col1, channel_col2 = st.columns(2)

with channel_col1:
    # Create sample data for ROI by channel
    channel_data = pd.DataFrame({
        'Channel': ['Webinars', 'Trade Shows', 'Content Marketing', 'SEO', 'Email Marketing', 'Paid Search', 'Social Media'],
        'Investment': [120000, 85000, 65000, 45000, 30000, 50000, 30000],
        'Revenue': [540000, 320000, 280000, 260000, 190000, 180000, 100000]
    })
    
    channel_data['ROI'] = (channel_data['Revenue'] - channel_data['Investment']) / channel_data['Investment']
    
    fig = px.bar(
        channel_data,
        x='Channel',
        y='ROI',
        color='ROI',
        text_auto='.1f',
        title="ROI by Marketing Channel"
    )
    fig.update_traces(texttemplate='%{text}x', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

with channel_col2:
    # Investment vs. Revenue
    fig = px.scatter(
        channel_data,
        x='Investment',
        y='Revenue',
        size='Revenue',
        color='Channel',
        text='Channel',
        title="Investment vs. Revenue by Channel",
        labels={'Investment': 'Investment ($)', 'Revenue': 'Revenue ($)'}
    )
    
    # Add ROI reference lines
    roi_values = [1, 2, 3, 5, 10]
    for roi in roi_values:
        fig.add_shape(
            type="line",
            y0=0,
            x0=0,
            y1=channel_data['Investment'].max() * roi * 1.2,
            x1=channel_data['Investment'].max() / roi,
            line=dict(color="gray", dash="dot")
        )
        fig.add_annotation(
            x=channel_data['Investment'].max() / roi / 2,
            y=channel_data['Investment'].max() / roi / 2 * roi,
            text=f"ROI = {roi}x",
            showarrow=False,
            font=dict(color="gray")
        )
    
    st.plotly_chart(fig, use_container_width=True)

# ROI for Webinar Program
st.header("Webinar Program ROI Analysis")
webinar_col1, webinar_col2 = st.columns(2)

with webinar_col1:
    # Create sample data for webinar ROI
    webinar_data = pd.DataFrame({
        'Webinar': [
            'Product Demo Series', 
            'Industry Trend Updates', 
            'Clinical Application Training',
            'Customer Success Stories',
            'Partner Collaboration Series'
        ],
        'Attendees': [320, 280, 180, 210, 150],
        'Leads': [280, 240, 160, 190, 120],
        'Opportunities': [56, 48, 32, 38, 24],
        'Revenue': [224000, 192000, 128000, 152000, 96000],
        'Cost': [45000, 40000, 32000, 38000, 30000]
    })
    
    webinar_data['ROI'] = (webinar_data['Revenue'] - webinar_data['Cost']) / webinar_data['Cost']
    webinar_data['Cost_per_Lead'] = webinar_data['Cost'] / webinar_data['Leads']
    
    fig = px.bar(
        webinar_data,
        x='Webinar',
        y='ROI',
        color='ROI',
        text_auto='.1f',
        title="ROI by Webinar Series"
    )
    fig.update_traces(texttemplate='%{text}x', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

with webinar_col2:
    # Webinar funnel analysis
    webinar_funnel = pd.DataFrame({
        'Stage': ['Invited', 'Registered', 'Attended', 'MQL', 'SQL', 'Opportunity', 'Won'],
        'Count': [5000, 1200, 800, 600, 300, 150, 60]
    })
    
    fig = px.funnel(
        webinar_funnel,
        x='Count',
        y='Stage',
        title="Webinar Program Conversion Funnel"
    )
    st.plotly_chart(fig, use_container_width=True)

# ROI Over Time
st.header("Marketing ROI Trends")

# Create sample data for ROI over time
dates = pd.date_range(start='2023-01-01', periods=12, freq='M')
channels = ['Webinars', 'Trade Shows', 'Content Marketing', 'Email', 'Paid Media']

roi_trend_data = pd.DataFrame()
for channel in channels:
    # Generate slightly different ROI trend patterns for each channel
    if channel == 'Webinars':
        roi_values = np.linspace(3.8, 5.2, len(dates)) + np.random.normal(0, 0.3, len(dates))
    elif channel == 'Trade Shows':
        roi_values = np.linspace(3.5, 2.8, len(dates)) + np.random.normal(0, 0.3, len(dates))
    elif channel == 'Content Marketing':
        roi_values = np.linspace(4.0, 4.8, len(dates)) + np.random.normal(0, 0.2, len(dates))
    elif channel == 'Email':
        roi_values = np.linspace(5.5, 6.2, len(dates)) + np.random.normal(0, 0.4, len(dates))
    else:  # Paid Media
        roi_values = np.linspace(2.8, 3.5, len(dates)) + np.random.normal(0, 0.3, len(dates))
    
    channel_data = pd.DataFrame({
        'Date': dates,
        'Channel': channel,
        'ROI': roi_values
    })
    roi_trend_data = pd.concat([roi_trend_data, channel_data])

fig = px.line(
    roi_trend_data,
    x='Date',
    y='ROI',
    color='Channel',
    title="ROI Trends by Marketing Channel"
)
st.plotly_chart(fig, use_container_width=True)

# ROI Forecasting
st.header("ROI Forecasting & Optimization")
forecast_col1, forecast_col2 = st.columns(2)

with forecast_col1:
    # Budget allocation optimizer
    st.subheader("Budget Allocation Optimizer")
    
    # Sample current vs. optimized allocation
    allocation_data = pd.DataFrame({
        'Channel': ['Webinars', 'Trade Shows', 'Content', 'SEO', 'Email', 'Paid Search', 'Social'],
        'Current Allocation': [28, 20, 15, 11, 7, 12, 7],
        'Optimized Allocation': [33, 16, 18, 13, 10, 8, 2]
    })
    
    allocation_data_long = pd.melt(
        allocation_data, 
        id_vars=['Channel'],
        value_vars=['Current Allocation', 'Optimized Allocation'],
        var_name='Allocation Type',
        value_name='Percentage'
    )
    
    fig = px.bar(
        allocation_data_long,
        x='Channel',
        y='Percentage',
        color='Allocation Type',
        barmode='group',
        title="Current vs. Optimized Budget Allocation (%)",
        text_auto=True
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Expected impact
    impact_data = pd.DataFrame({
        'Metric': ['Total ROI', 'Lead Volume', 'Cost per Lead', 'Revenue'],
        'Current': [4.4, 1200, 105, 1870000],
        'Optimized': [5.1, 1320, 92, 2080000],
        'Change': ['+15.9%', '+10.0%', '-12.4%', '+11.2%']
    })
    
    st.subheader("Expected Impact of Optimized Allocation")
    st.dataframe(impact_data, use_container_width=True)

with forecast_col2:
    # ROI sensitivity analysis
    st.subheader("ROI Sensitivity Analysis")
    
    # Create sensitivity analysis data
    sensitivity_data = pd.DataFrame({
        'Budget_Change': np.arange(-30, 35, 5),
        'Webinars': [2.8, 3.1, 3.4, 3.7, 4.0, 4.4, 4.7, 5.0, 5.2, 5.3, 5.4, 5.5, 5.5],
        'Trade_Shows': [2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.1, 3.2, 3.3, 3.3, 3.2, 3.1, 3.0],
        'Content': [3.5, 3.7, 3.9, 4.1, 4.3, 4.5, 4.7, 4.8, 4.9, 5.0, 5.0, 5.0, 5.0],
        'Email': [5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.1, 6.2, 6.3, 6.3, 6.3, 6.2, 6.1]
    })
    
    fig = px.line(
        sensitivity_data,
        x='Budget_Change',
        y=['Webinars', 'Trade_Shows', 'Content', 'Email'],
        title="ROI Sensitivity to Budget Changes",
        labels={'Budget_Change': 'Budget Change (%)', 'value': 'ROI'}
    )
    
    # Add vertical line at 0% change
    fig.add_vline(x=0, line_dash="dash", line_color="gray")
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("""
    **Analysis Insights:**
    - Webinars and Content Marketing show strong ROI growth potential with additional investment
    - Trade Shows reach diminishing returns after 10% budget increase
    - Email marketing maintains high ROI across budget scenarios
    - Recommended: Increase webinar budget by 15-20% for optimal returns
    """)

# ROI by Campaign
st.header("Campaign-Level ROI Analysis")

# Create sample campaign ROI data
campaign_data = pd.DataFrame({
    'Campaign': [
        'Q1 Product Launch', 
        'Healthcare Conference Series', 
        'Summer Webinar Series',
        'Competitive Replacement Program',
        'Customer Education Series',
        'End of Year Promotion',
        'Digital Transformation Summit',
        'Industry Awards Sponsorship'
    ],
    'Investment': [85000, 120000, 60000, 45000, 35000, 50000, 70000, 40000],
    'Pipeline': [425000, 540000, 300000, 270000, 175000, 200000, 315000, 160000],
    'Closed Revenue': [170000, 240000, 120000, 135000, 90000, 85000, 110000, 65000],
    'Timeline': ['Q1', 'Q1-Q2', 'Q2', 'Q2-Q3', 'Q3', 'Q4', 'Q3', 'Q4']
})

campaign_data['ROI'] = campaign_data['Closed Revenue'] / campaign_data['Investment']
campaign_data['Pipeline Ratio'] = campaign_data['Pipeline'] / campaign_data['Investment']

# Campaign ROI chart
fig = px.scatter(
    campaign_data,
    x='Investment',
    y='ROI',
    size='Closed Revenue',
    color='Timeline',
    text='Campaign',
    title="Campaign ROI Analysis",
    height=500
)
fig.update_traces(textposition='top center')
st.plotly_chart(fig, use_container_width=True)

# Campaign performance table with formatting
st.subheader("Campaign Performance Details")
campaign_display = campaign_data.copy()
campaign_display['Investment'] = campaign_display['Investment'].apply(lambda x: f"${x:,.0f}")
campaign_display['Pipeline'] = campaign_display['Pipeline'].apply(lambda x: f"${x:,.0f}")
campaign_display['Closed Revenue'] = campaign_display['Closed Revenue'].apply(lambda x: f"${x:,.0f}")
campaign_display['ROI'] = campaign_display['ROI'].apply(lambda x: f"{x:.2f}x")
campaign_display['Pipeline Ratio'] = campaign_display['Pipeline Ratio'].apply(lambda x: f"{x:.2f}x")

st.dataframe(campaign_display, use_container_width=True)
