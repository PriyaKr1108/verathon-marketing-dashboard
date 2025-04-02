import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="Digital Marketing Dashboard", page_icon="📊", layout="wide")

# Dashboard title
st.title("Digital Marketing Dashboard")

# Time period filter
time_period = st.selectbox(
    "Select Time Period",
    ["Last 7 Days", "Last 30 Days", "Last Quarter", "Year to Date", "Custom"]
)

if time_period == "Custom":
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime.now() - timedelta(days=30))
    with col2:
        end_date = st.date_input("End Date", datetime.now())

# Main dashboard layout
top_kpi_col1, top_kpi_col2, top_kpi_col3, top_kpi_col4 = st.columns(4)

# Sample KPI metrics
with top_kpi_col1:
    st.metric(label="Website Visitors", value="24,589", delta="12.7%")
    
with top_kpi_col2:
    st.metric(label="Conversion Rate", value="3.2%", delta="0.5%")
    
with top_kpi_col3:
    st.metric(label="MQLs", value="583", delta="-2.1%", delta_color="inverse")
    
with top_kpi_col4:
    st.metric(label="Cost per MQL", value="$42.18", delta="-8.3%", delta_color="inverse")

# Tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs(["Traffic Analytics", "Conversion Funnel", "Channel Effectiveness", "Campaign Performance"])

with tab1:
    st.subheader("Traffic Source Analysis")
    
    # Sample data for traffic sources
    source_data = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=90, freq='D'),
        'Organic Search': np.random.randint(500, 1500, 90),
        'Direct': np.random.randint(300, 800, 90),
        'Referral': np.random.randint(200, 600, 90),
        'Social Media': np.random.randint(100, 400, 90),
        'Email': np.random.randint(50, 250, 90),
        'Paid Search': np.random.randint(150, 500, 90)
    })
    
    fig = px.line(
        source_data, 
        x='Date', 
        y=['Organic Search', 'Direct', 'Referral', 'Social Media', 'Email', 'Paid Search'],
        title='Daily Traffic by Source'
    )
    
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Visitors',
        legend_title='Source',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top Landing Pages")
        landing_pages = pd.DataFrame({
            'Page': [
                '/products/new-device', 
                '/solutions/healthcare', 
                '/blog/medical-innovation',
                '/about-verathon',
                '/contact'
            ],
            'Visitors': [3245, 2891, 1654, 1432, 987],
            'Bounce Rate': [32.4, 28.7, 45.2, 39.1, 22.8]
        })
        
        st.dataframe(landing_pages, hide_index=True, use_container_width=True)
    
    with col2:
        st.subheader("Geographic Distribution")
        geo_data = pd.DataFrame({
            'Country': ['United States', 'Canada', 'United Kingdom', 'Germany', 'Australia', 'France', 'Japan', 'Other'],
            'Visitors': [12453, 3245, 2876, 1765, 1342, 876, 765, 1267]
        })
        
        fig = px.pie(
            geo_data, 
            values='Visitors', 
            names='Country',
            title='Visitors by Country'
        )
        
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Marketing Funnel Analysis")
    
    funnel_stages = ['Website Visitors', 'Product Page Views', 'Form Fills', 'MQLs', 'SQLs', 'Opportunities', 'Closed Won']
    funnel_values = [24589, 12345, 2468, 583, 291, 87, 32]
    
    fig = go.Figure(go.Funnel(
        y=funnel_stages,
        x=funnel_values,
        textinfo="value+percent initial",
        marker={"color": ["#0056A7", "#1268B9", "#247ACC", "#368CDE", "#489EF1", "#5AB0FF", "#6BC2FF"]}
    ))
    
    fig.update_layout(
        title="Marketing Conversion Funnel",
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Conversion by Device")
        
        device_data = pd.DataFrame({
            'Device': ['Desktop', 'Mobile', 'Tablet'],
            'Visitors': [14753, 8234, 1602],
            'Conversions': [442, 123, 18],
            'Rate': [3.0, 1.5, 1.1]
        })
        
        device_data['Rate'] = device_data['Rate'].astype(str) + '%'
        st.dataframe(device_data, hide_index=True, use_container_width=True)
    
    with col2:
        st.subheader("Form Completion Analysis")
        
        form_data = pd.DataFrame({
            'Form': ['Contact Us', 'Product Demo', 'Whitepaper Download', 'Newsletter Signup'],
            'Starts': [1245, 876, 654, 432],
            'Completions': [623, 438, 523, 389],
            'Rate': [50.0, 50.0, 79.9, 90.0]
        })
        
        form_data['Rate'] = form_data['Rate'].astype(str) + '%'
        st.dataframe(form_data, hide_index=True, use_container_width=True)

with tab3:
    st.subheader("Channel Performance Analysis")
    
    channel_data = pd.DataFrame({
        'Channel': ['Organic Search', 'Paid Search', 'Email', 'Social Media', 'Direct', 'Referral'],
        'Visitors': [10234, 5621, 2145, 3256, 2568, 765],
        'MQLs': [256, 183, 72, 43, 23, 6],
        'Conv. Rate': [2.5, 3.2, 3.4, 1.3, 0.9, 0.8],
        'Cost': [0, 15432, 5400, 7200, 0, 800],
        'CPL': [0, 84.33, 75.00, 167.44, 0, 133.33]
    })
    
    fig = px.bar(
        channel_data,
        x='Channel',
        y=['Visitors', 'MQLs'],
        barmode='group',
        title='Traffic and Leads by Channel',
        labels={'value': 'Count', 'variable': 'Metric'}
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(
            channel_data,
            x='Channel',
            y='Conv. Rate',
            title='Conversion Rate by Channel (%)',
            color='Channel',
            labels={'Conv. Rate': 'Conversion Rate (%)'}
        )
        
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Filter out channels with zero cost
        cost_data = channel_data[channel_data['Cost'] > 0]
        
        fig = px.bar(
            cost_data,
            x='Channel',
            y='CPL',
            title='Cost per Lead by Channel ($)',
            color='Channel',
            labels={'CPL': 'Cost per Lead ($)'}
        )
        
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("Campaign Performance Metrics")
    
    campaign_data = pd.DataFrame({
        'Campaign': [
            'New Product Launch', 
            'Healthcare Conference', 
            'Q1 Email Nurture', 
            'Retargeting Ads',
            'Medical Blog Promotion', 
            'Partner Webinar'
        ],
        'Status': ['Active', 'Completed', 'Active', 'Active', 'Paused', 'Completed'],
        'Budget': [25000, 15000, 5000, 10000, 3000, 2000],
        'Spend': [12500, 15000, 3750, 8000, 1500, 2000],
        'Leads': [145, 87, 62, 93, 18, 32],
        'Opportunities': [12, 8, 5, 7, 1, 3],
        'Revenue': [180000, 120000, 75000, 95000, 15000, 40000],
        'ROI': [14.4, 8.0, 20.0, 11.9, 10.0, 20.0]
    })
    
    campaign_data['Spend %'] = (campaign_data['Spend'] / campaign_data['Budget'] * 100).round(1)
    campaign_data['CPL'] = (campaign_data['Spend'] / campaign_data['Leads']).round(2)
    campaign_data['ROI'] = campaign_data['ROI'].astype(str) + 'x'
    
    # Format columns for display
    display_data = campaign_data.copy()
    display_data['Budget'] = display_data['Budget'].apply(lambda x: f"${x:,}")
    display_data['Spend'] = display_data['Spend'].apply(lambda x: f"${x:,}")
    display_data['Revenue'] = display_data['Revenue'].apply(lambda x: f"${x:,}")
    display_data['Spend %'] = display_data['Spend %'].astype(str) + '%'
    display_data['CPL'] = display_data['CPL'].apply(lambda x: f"${x}")
    
    st.dataframe(display_data, hide_index=True, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(
            campaign_data,
            x='Campaign',
            y='Leads',
            color='Status',
            title='Leads Generated by Campaign',
            labels={'Leads': 'Number of Leads'}
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.scatter(
            campaign_data,
            x='Spend',
            y='Revenue',
            size='Leads',
            color='Campaign',
            title='Campaign ROI Analysis',
            labels={
                'Spend': 'Total Spend ($)',
                'Revenue': 'Revenue Generated ($)',
                'Leads': 'Number of Leads'
            }
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Digital Marketing Maturity Framework section
st.markdown("---")
st.subheader("Digital Marketing Growth Maturity Assessment")

col1, col2 = st.columns([3, 2])

with col1:
    maturity_categories = [
        'Analytics Implementation', 
        'Content Strategy', 
        'Marketing Automation', 
        'Lead Scoring', 
        'Attribution Modeling',
        'Personalization',
        'SEO Strategy'
    ]
    
    maturity_levels = {
        'Current': [2, 1, 1, 0, 0, 1, 2],
        'Target Q2': [2, 2, 2, 1, 1, 2, 2],
        'Target EOY': [3, 3, 3, 2, 2, 3, 3]
    }
    
    # Create radar chart
    fig = go.Figure()
    
    # Add traces for current and targets
    fig.add_trace(go.Scatterpolar(
        r=maturity_levels['Current'],
        theta=maturity_categories,
        fill='toself',
        name='Current'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=maturity_levels['Target Q2'],
        theta=maturity_categories,
        fill='toself',
        name='Target Q2'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=maturity_levels['Target EOY'],
        theta=maturity_categories,
        fill='toself',
        name='Target EOY'
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
        title="Digital Marketing Maturity Progression",
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("### Maturity Levels")
    st.markdown("""
    **Level 0: Not Implemented**
    - No formalized processes or tools in place
    
    **Level 1: Crawl**
    - Basic implementation
    - Manual processes
    - Limited reporting
    
    **Level 2: Walk**
    - Standardized processes
    - Partial automation
    - Regular reporting and analytics
    
    **Level 3: Run**
    - Fully automated processes
    - Advanced analytics
    - AI-driven optimization
    - Continuous improvement
    """)
    
    st.markdown("### Recommended Next Steps")
    st.info("1. Implement marketing automation for email nurture campaigns")
    st.info("2. Develop basic lead scoring model based on website behavior")
    st.info("3. Enhance content strategy with persona-specific content")
