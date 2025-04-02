import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="Webinar Management", page_icon="🎥", layout="wide")

# Dashboard title
st.title("Webinar Management Dashboard")

# Filter section
col1, col2, col3 = st.columns(3)

with col1:
    webinar_status = st.selectbox(
        "Webinar Status",
        ["All", "Upcoming", "Completed", "In Progress"]
    )

with col2:
    date_range = st.selectbox(
        "Date Range",
        ["Last 30 Days", "Last Quarter", "Last 6 Months", "Year to Date", "All Time"]
    )

with col3:
    webinar_type = st.multiselect(
        "Webinar Type",
        ["Product Demo", "Thought Leadership", "Educational", "Customer Stories", "Partner Webinars"],
        default=["Product Demo", "Thought Leadership", "Educational"]
    )

# Webinar program KPIs
st.markdown("### Webinar Program KPIs")
kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

with kpi1:
    st.metric(label="Total Webinars", value="24", delta="4")

with kpi2:
    st.metric(label="Total Registrations", value="3,256", delta="12.4%")

with kpi3:
    st.metric(label="Avg. Attendance Rate", value="42%", delta="3.5%")

with kpi4:
    st.metric(label="Lead Conversion", value="18.2%", delta="-0.8%", delta_color="inverse")

with kpi5:
    st.metric(label="Cost per Lead", value="$42.18", delta="-5.3%", delta_color="inverse")

# Tabs for different sections
tab1, tab2, tab3 = st.tabs(["Webinar Overview", "Performance Analysis", "Maturity Framework"])

with tab1:
    # Upcoming webinars
    st.subheader("Upcoming Webinars")
    
    upcoming_webinars = pd.DataFrame({
        'Webinar Name': [
            'New Product Launch: XYZ Medical Device', 
            'Healthcare Trends 2024', 
            'Regulatory Compliance Update', 
            'Customer Success Story: Memorial Hospital'
        ],
        'Date': ['May 15, 2024', 'June 2, 2024', 'June 18, 2024', 'July 10, 2024'],
        'Type': ['Product Demo', 'Thought Leadership', 'Educational', 'Customer Stories'],
        'Current Registrations': [124, 87, 45, 12],
        'Registration Goal': [200, 150, 100, 50],
        'Status': ['On Track', 'Needs Attention', 'At Risk', 'Just Announced']
    })
    
    # Function to style the dataframe
    def highlight_status(val):
        if val == 'On Track':
            return 'background-color: #d4edda; color: #155724'
        elif val == 'Needs Attention':
            return 'background-color: #fff3cd; color: #856404'
        elif val == 'At Risk':
            return 'background-color: #f8d7da; color: #721c24'
        else:
            return 'background-color: #d1ecf1; color: #0c5460'
    
    st.dataframe(upcoming_webinars.style.applymap(highlight_status, subset=['Status']), hide_index=True, use_container_width=True)
    
    # Past webinars performance
    st.subheader("Recent Webinar Performance")
    
    past_webinars = pd.DataFrame({
        'Webinar Name': [
            'Medical Device Innovations', 
            'Healthcare Marketing Strategies', 
            'Patient Engagement Solutions', 
            'Digital Transformation in Healthcare',
            'Supply Chain Optimization'
        ],
        'Date': ['Apr 12, 2024', 'Mar 28, 2024', 'Mar 15, 2024', 'Feb 22, 2024', 'Feb 8, 2024'],
        'Registrations': [187, 212, 156, 198, 142],
        'Attendees': [92, 96, 74, 82, 61],
        'Attendance Rate': ['49%', '45%', '47%', '41%', '43%'],
        'MQLs Generated': [34, 42, 28, 36, 22],
        'MQL Conversion': ['18.2%', '19.8%', '17.9%', '18.2%', '15.5%']
    })
    
    st.dataframe(past_webinars, hide_index=True, use_container_width=True)
    
    # Registration trends chart
    st.subheader("Registration Trends")
    
    # Sample data for trends
    trend_data = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=16, freq='W'),
        'Registrations': [87, 95, 82, 78, 92, 110, 105, 112, 128, 145, 132, 156, 187, 212, 198, 124],
        'Attendees': [38, 42, 35, 36, 44, 52, 49, 48, 58, 63, 57, 72, 92, 96, 82, 0]
    })
    
    # Add moving averages
    trend_data['Reg_4W_Avg'] = trend_data['Registrations'].rolling(window=4).mean()
    trend_data['Att_4W_Avg'] = trend_data['Attendees'].rolling(window=4).mean()
    
    fig = px.line(
        trend_data, 
        x='Date', 
        y=['Registrations', 'Attendees', 'Reg_4W_Avg', 'Att_4W_Avg'],
        title='Webinar Registration and Attendance Trends',
        labels={'value': 'Count', 'variable': 'Metric'},
        line_shape='spline'
    )
    
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Registration by Webinar Type")
        
        type_data = pd.DataFrame({
            'Type': ['Product Demo', 'Thought Leadership', 'Educational', 'Customer Stories', 'Partner Webinars'],
            'Registrations': [1245, 876, 654, 321, 160],
            'Avg per Webinar': [155.6, 146.0, 109.0, 80.3, 53.3]
        })
        
        fig = px.bar(
            type_data,
            x='Type',
            y='Registrations',
            color='Type',
            title='Total Registrations by Webinar Type',
            text='Registrations'
        )
        
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Attendance Rate by Webinar Type")
        
        attendance_data = pd.DataFrame({
            'Type': ['Product Demo', 'Thought Leadership', 'Educational', 'Customer Stories', 'Partner Webinars'],
            'Attendance Rate': [45, 48, 52, 39, 37]
        })
        
        fig = px.bar(
            attendance_data,
            x='Type',
            y='Attendance Rate',
            color='Type',
            title='Average Attendance Rate by Webinar Type (%)',
            text='Attendance Rate'
        )
        
        fig.update_layout(showlegend=False)
        fig.update_traces(texttemplate='%{text}%', textposition='outside')
        fig.update_yaxes(range=[0, 60])
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Lead Generation Performance")
    
    lead_data = pd.DataFrame({
        'Webinar Name': [
            'Medical Device Innovations', 
            'Healthcare Marketing Strategies', 
            'Patient Engagement Solutions', 
            'Digital Transformation in Healthcare',
            'Supply Chain Optimization',
            'Regulatory Compliance Updates',
            'Healthcare Data Security',
            'Remote Patient Monitoring'
        ],
        'Date': [
            'Apr 12, 2024', 
            'Mar 28, 2024', 
            'Mar 15, 2024', 
            'Feb 22, 2024', 
            'Feb 8, 2024',
            'Jan 25, 2024',
            'Jan 11, 2024',
            'Dec 14, 2023'
        ],
        'Registrations': [187, 212, 156, 198, 142, 165, 178, 145],
        'MQLs': [34, 42, 28, 36, 22, 31, 33, 27],
        'SQLs': [12, 16, 8, 15, 6, 10, 12, 9],
        'Opportunities': [4, 5, 2, 3, 1, 2, 3, 2],
        'Closed Won': [1, 2, 0, 1, 0, 1, 1, 1]
    })
    
    # Calculate conversion rates
    lead_data['MQL Rate'] = (lead_data['MQLs'] / lead_data['Registrations'] * 100).round(1)
    lead_data['SQL Rate'] = (lead_data['SQLs'] / lead_data['MQLs'] * 100).round(1)
    
    # Create a funnel chart for the overall pipeline
    total_funnel = {
        'Stage': ['Registrations', 'MQLs', 'SQLs', 'Opportunities', 'Closed Won'],
        'Count': [
            lead_data['Registrations'].sum(),
            lead_data['MQLs'].sum(),
            lead_data['SQLs'].sum(), 
            lead_data['Opportunities'].sum(),
            lead_data['Closed Won'].sum()
        ]
    }
    
    fig = go.Figure(go.Funnel(
        y=total_funnel['Stage'],
        x=total_funnel['Count'],
        textinfo="value+percent initial",
        marker={"color": ["#0056A7", "#1268B9", "#247ACC", "#368CDE", "#489EF1"]}
    ))
    
    fig.update_layout(
        title="Webinar Lead Conversion Funnel",
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("MQL Conversion Rate by Webinar")
        
        fig = px.bar(
            lead_data.sort_values('MQL Rate', ascending=False),
            x='Webinar Name',
            y='MQL Rate',
            color='MQL Rate',
            title='MQL Conversion Rate (%)',
            labels={'MQL Rate': 'MQL Conversion (%)'},
            text='MQL Rate'
        )
        
        fig.update_layout(showlegend=False, xaxis_tickangle=-45)
        fig.update_traces(texttemplate='%{text}%', textposition='outside')
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("SQL Conversion Rate by Webinar")
        
        fig = px.bar(
            lead_data.sort_values('SQL Rate', ascending=False),
            x='Webinar Name',
            y='SQL Rate',
            color='SQL Rate',
            title='SQL Conversion Rate (%)',
            labels={'SQL Rate': 'SQL Conversion (%)'},
            text='SQL Rate'
        )
        
        fig.update_layout(showlegend=False, xaxis_tickangle=-45)
        fig.update_traces(texttemplate='%{text}%', textposition='outside')
        
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Webinar Program Maturity Framework")
    
    st.markdown("""
    The Digital Factory 24 Webinar Maturity Framework helps organizations assess and improve their webinar program 
    through three stages of maturity: Crawl, Walk, and Run.
    """)
    
    # Maturity stages
    stages = {
        "Crawl": {
            "Technology": ["Basic webinar platform", "Manual registration process", "Standard templates", "Limited analytics"],
            "Content": ["Generic presentations", "Minimal audience engagement", "Limited follow-up", "Basic promotion"],
            "Process": ["Ad-hoc planning", "Manual lead routing", "Basic metrics tracking", "No formal strategy"]
        },
        "Walk": {
            "Technology": ["Integration with marketing automation", "Semi-automated workflows", "Custom branding", "Enhanced analytics"],
            "Content": ["Segmented content strategy", "Interactive presentations", "Structured follow-up", "Multi-channel promotion"],
            "Process": ["Standardized planning", "Automated lead routing", "Regular reporting", "Quarterly strategy"]
        },
        "Run": {
            "Technology": ["Full marketing tech stack integration", "AI-driven personalization", "Advanced production quality", "Predictive analytics"],
            "Content": ["Personalized content journeys", "Multi-format engagement", "Automated nurture paths", "Integrated campaigns"],
            "Process": ["Continuous optimization", "Closed-loop analytics", "Revenue attribution", "Integrated program strategy"]
        }
    }
    
    # Show maturity framework in expandable sections
    for stage, categories in stages.items():
        with st.expander(f"{stage} Stage", expanded=(stage == "Crawl")):
            for category, items in categories.items():
                st.markdown(f"**{category}**")
                for item in items:
                    st.markdown(f"- {item}")
    
    # Current maturity assessment
    st.subheader("Current Maturity Assessment")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        categories = ['Technology Stack', 'Content Strategy', 'Audience Engagement', 'Lead Management', 'Analytics', 'Follow-up Process', 'Program Integration']
        
        maturity_levels = {
            'Current': [1, 2, 1, 1, 0, 1, 0],
            'Target Q2': [2, 2, 2, 2, 1, 2, 1],
            'Target EOY': [2, 3, 2, 3, 2, 2, 2]
        }
        
        # Create radar chart
        fig = go.Figure()
        
        # Add traces for current and targets
        fig.add_trace(go.Scatterpolar(
            r=maturity_levels['Current'],
            theta=categories,
            fill='toself',
            name='Current'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=maturity_levels['Target Q2'],
            theta=categories,
            fill='toself',
            name='Target Q2'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=maturity_levels['Target EOY'],
            theta=categories,
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
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Key Improvement Areas")
        
        improvements = [
            {
                "area": "Analytics Implementation",
                "current": "Basic attendance tracking only",
                "recommendation": "Implement attendee engagement scoring and post-webinar behavioral tracking"
            },
            {
                "area": "Lead Management",
                "current": "Manual lead qualification",
                "recommendation": "Implement automated lead scoring based on webinar engagement and follow-up actions"
            },
            {
                "area": "Program Integration",
                "current": "Standalone webinars",
                "recommendation": "Integrate webinars into full content marketing and nurture programs"
            }
        ]
        
        for item in improvements:
            st.markdown(f"**{item['area']}**")
            st.markdown(f"*Current State:* {item['current']}")
            st.markdown(f"*Recommendation:* {item['recommendation']}")
            st.markdown("---")
    
    # Implementation roadmap
    st.subheader("Implementation Roadmap")
    
    roadmap_data = pd.DataFrame({
        'Task': [
            'Implement marketing automation integration',
            'Develop engagement scoring system',
            'Create content strategy template',
            'Build automated follow-up workflows',
            'Implement lead scoring model',
            'Develop webinar program analytics dashboard',
            'Create integrated promotional plan',
            'Implement A/B testing framework'
        ],
        'Stage': ['Crawl→Walk', 'Crawl→Walk', 'Crawl→Walk', 'Walk', 'Walk', 'Walk', 'Walk→Run', 'Walk→Run'],
        'Priority': ['High', 'High', 'Medium', 'High', 'Medium', 'Low', 'Medium', 'Low'],
        'Estimated Timeline': ['Q2 2024', 'Q2 2024', 'Q2 2024', 'Q3 2024', 'Q3 2024', 'Q3 2024', 'Q4 2024', 'Q4 2024'],
        'Status': ['In Progress', 'Not Started', 'Not Started', 'Not Started', 'Not Started', 'Not Started', 'Not Started', 'Not Started']
    })
    
    # Function to color the status
    def color_status(val):
        if val == 'Completed':
            return 'background-color: #d4edda; color: #155724'
        elif val == 'In Progress':
            return 'background-color: #fff3cd; color: #856404'
        else:
            return 'background-color: #f8d7da; color: #721c24'
    
    st.dataframe(roadmap_data.style.applymap(color_status, subset=['Status']), hide_index=True, use_container_width=True)
