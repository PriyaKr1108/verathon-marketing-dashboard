import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np
import json

# Page configuration
st.set_page_config(
    page_title="Marketing Automation - Verathon",
    page_icon="⚙️",
    layout="wide"
)

# Header
st.title("Marketing Automation Workflows")
st.markdown("Build, manage, and optimize your marketing automation workflows")

# Workflow Builder Section
st.header("Workflow Builder")

# Sidebar for workflow elements
with st.sidebar:
    st.header("Workflow Elements")
    st.subheader("Triggers")
    
    st.button("Form Submission", key="trigger_form")
    st.button("Website Visit", key="trigger_visit")
    st.button("Email Interaction", key="trigger_email")
    st.button("Webinar Registration", key="trigger_webinar")
    st.button("CRM Status Change", key="trigger_crm")
    
    st.subheader("Actions")
    
    st.button("Send Email", key="action_email")
    st.button("Add to List", key="action_list")
    st.button("Update CRM", key="action_crm")
    st.button("Notify Sales", key="action_notify")
    st.button("Wait", key="action_wait")
    
    st.subheader("Conditions")
    
    st.button("If/Else Branch", key="condition_if")
    st.button("Segment Split", key="condition_segment")
    st.button("Lead Score Check", key="condition_score")

# Main workflow canvas
workflow_col1, workflow_col2 = st.columns([3, 1])

with workflow_col1:
    # Workflow Canvas
    st.subheader("Workflow Canvas")
    
    # Sample workflow JSON representation
    sample_workflow = {
        "name": "Webinar Lead Nurturing",
        "status": "active",
        "steps": [
            {"id": 1, "type": "trigger", "name": "Webinar Registration", "position": {"x": 100, "y": 100}},
            {"id": 2, "type": "action", "name": "Send Confirmation Email", "position": {"x": 100, "y": 200}},
            {"id": 3, "type": "action", "name": "Wait 1 Day", "position": {"x": 100, "y": 300}},
            {"id": 4, "type": "action", "name": "Send Reminder Email", "position": {"x": 100, "y": 400}},
            {"id": 5, "type": "condition", "name": "Check Attendance", "position": {"x": 100, "y": 500}},
            {"id": 6, "type": "action", "name": "Send Thank You + Resources", "position": {"x": 250, "y": 600}},
            {"id": 7, "type": "action", "name": "Send Missed You + Recording", "position": {"x": 0, "y": 600}},
            {"id": 8, "type": "action", "name": "Wait 3 Days", "position": {"x": 100, "y": 700}},
            {"id": 9, "type": "action", "name": "Send Follow-up Survey", "position": {"x": 100, "y": 800}},
            {"id": 10, "type": "condition", "name": "Lead Score Check", "position": {"x": 100, "y": 900}},
            {"id": 11, "type": "action", "name": "Notify Sales Rep", "position": {"x": 250, "y": 1000}},
            {"id": 12, "type": "action", "name": "Continue Nurturing", "position": {"x": 0, "y": 1000}}
        ],
        "connections": [
            {"from": 1, "to": 2},
            {"from": 2, "to": 3},
            {"from": 3, "to": 4},
            {"from": 4, "to": 5},
            {"from": 5, "to": 6, "label": "Attended"},
            {"from": 5, "to": 7, "label": "Did Not Attend"},
            {"from": 6, "to": 8},
            {"from": 7, "to": 8},
            {"from": 8, "to": 9},
            {"from": 9, "to": 10},
            {"from": 10, "to": 11, "label": "High Score (>80)"},
            {"from": 10, "to": 12, "label": "Low Score (<80)"}
        ]
    }
    
    # This is a simplified representation - in a real app, this would be a canvas
    # with draggable elements rendered with a specialized library
    st.image("https://images.unsplash.com/photo-1507925921958-8a62f3d1a50d", 
             caption="Marketing Workflow Canvas - Webinar Lead Nurturing")
    
    st.info("Drag and drop elements from the sidebar to build your workflow. Connect elements to create a complete automation flow.")
    
    st.subheader("Workflow JSON Preview")
    st.json(sample_workflow)

with workflow_col2:
    # Workflow Properties
    st.subheader("Workflow Properties")
    
    st.text_input("Workflow Name", value="Webinar Lead Nurturing")
    
    st.selectbox(
        "Status",
        ["Draft", "Active", "Paused", "Archived"]
    )
    
    st.text_area("Description", value="Nurture leads from webinar registration through post-event follow-up based on attendance and engagement.", height=100)
    
    st.subheader("Selected Element Properties")
    st.text_input("Element Name", value="Send Follow-up Survey")
    st.selectbox("Element Type", ["Trigger", "Action", "Condition"])
    
    st.button("Save Workflow")
    st.button("Test Workflow")
    st.button("Publish Workflow")

# Workflow Templates
st.header("Workflow Templates")
template_col1, template_col2, template_col3 = st.columns(3)

with template_col1:
    st.subheader("Webinar Lead Nurturing")
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4", 
             caption="Webinar Automation Workflow")
    st.markdown("""
    **Stages:**
    - Registration confirmation
    - Event reminders
    - Post-event follow-up
    - Survey & feedback
    - Lead scoring & routing
    """)
    st.button("Use Template", key="template1")

with template_col2:
    st.subheader("Product Interest Qualification")
    st.image("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40", 
             caption="Product Interest Workflow")
    st.markdown("""
    **Stages:**
    - Product page visit tracking
    - Resource delivery
    - Interest confirmation
    - Demo scheduling
    - Sales handoff
    """)
    st.button("Use Template", key="template2")

with template_col3:
    st.subheader("Event Follow-up Sequence")
    st.image("https://images.unsplash.com/photo-1519389950473-47ba0277781c", 
             caption="Event Follow-up Workflow")
    st.markdown("""
    **Stages:**
    - Post-event thank you
    - Content delivery
    - Segmented follow-up
    - Meeting scheduling
    - Feedback collection
    """)
    st.button("Use Template", key="template3")

# Active Workflows
st.header("Active Workflows")

# Generate sample workflow data
workflow_data = pd.DataFrame({
    'Workflow Name': [
        'Webinar Lead Nurturing', 
        'Trade Show Follow-up', 
        'Product Interest Sequence',
        'Customer Onboarding',
        'Re-engagement Campaign'
    ],
    'Status': ['Active', 'Active', 'Active', 'Paused', 'Draft'],
    'Created': [
        '2023-10-15',
        '2023-11-02',
        '2023-09-28',
        '2023-10-05',
        '2023-11-10'
    ],
    'Leads in Workflow': [124, 86, 215, 52, 0],
    'Conversion Rate': ['12.4%', '8.6%', '15.2%', '22.1%', 'N/A'],
    'Revenue Impact': ['$24,500', '$12,800', '$32,100', '$18,500', 'N/A']
})

st.dataframe(workflow_data, use_container_width=True)

# Workflow Performance
st.header("Workflow Performance Metrics")
workflow_perf_col1, workflow_perf_col2 = st.columns(2)

with workflow_perf_col1:
    # Conversion funnel
    funnel_data = pd.DataFrame({
        'Stage': ['Entered Workflow', 'Email Opened', 'Clicked Link', 'Visited Website', 'Requested Info', 'Converted to Opportunity'],
        'Count': [500, 400, 320, 250, 180, 120]
    })
    
    fig = px.funnel(
        funnel_data,
        x='Count',
        y='Stage',
        title="Workflow Conversion Funnel - Webinar Lead Nurturing"
    )
    st.plotly_chart(fig, use_container_width=True)

with workflow_perf_col2:
    # Workflow comparison
    comparison_data = pd.DataFrame({
        'Workflow': ['Webinar Nurturing', 'Trade Show', 'Product Interest', 'Customer Onboarding'],
        'Conversion Rate': [12.4, 8.6, 15.2, 22.1],
        'Avg Days to Conversion': [18, 24, 16, 12],
        'ROI': [3.2, 2.4, 3.8, 4.5]
    })
    
    fig = px.scatter(
        comparison_data,
        x='Avg Days to Conversion',
        y='Conversion Rate',
        size='ROI',
        color='Workflow',
        text='Workflow',
        title="Workflow Performance Comparison"
    )
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig, use_container_width=True)

# Integration Status
st.header("Marketing Automation Integrations")
integration_col1, integration_col2, integration_col3 = st.columns(3)

with integration_col1:
    st.subheader("CRM Integration")
    st.success("✅ Connected to Salesforce")
    st.markdown("""
    **Syncing:**
    - Contacts
    - Leads
    - Opportunities
    - Tasks
    - Custom objects
    """)
    st.button("Configure CRM Integration")

with integration_col2:
    st.subheader("Webinar Platform")
    st.success("✅ Connected to Cvent")
    st.markdown("""
    **Syncing:**
    - Event data
    - Registrations
    - Attendance
    - Engagement metrics
    - Follow-up actions
    """)
    st.button("Configure Webinar Integration")

with integration_col3:
    st.subheader("Website Tracking")
    st.success("✅ Tracking script installed")
    st.markdown("""
    **Tracking:**
    - Page visits
    - Form submissions
    - Custom events
    - Resource downloads
    - Video engagement
    """)
    st.button("Configure Website Tracking")

# Automation Rules
st.header("Lead Scoring & Routing Rules")
scoring_col1, scoring_col2 = st.columns(2)

with scoring_col1:
    st.subheader("Lead Scoring Rules")
    
    scoring_data = pd.DataFrame({
        'Activity': [
            'Webinar Registration', 
            'Webinar Attendance', 
            'Product Page Visit',
            'Pricing Page Visit',
            'Case Study Download',
            'Demo Request',
            'Email Click',
            'Form Submission'
        ],
        'Points': [5, 10, 3, 8, 15, 25, 2, 10]
    })
    
    st.dataframe(scoring_data, use_container_width=True)
    st.button("Edit Scoring Rules")

with scoring_col2:
    st.subheader("Lead Routing Rules")
    
    st.markdown("""
    **Routing Criteria:**
    
    1. **High Value Leads (Score > 50)**
       - Route to: Senior Sales Representatives
       - SLA: Contact within 4 hours
    
    2. **Medium Value Leads (Score 25-50)**
       - Route to: Inside Sales Team
       - SLA: Contact within 24 hours
       
    3. **Low Value Leads (Score < 25)**
       - Action: Continue nurturing via automation
       - Re-evaluate after score changes
    
    4. **Specific Product Interest**
       - Route based on product specialization
       - Consider territory assignments
    """)
    
    st.button("Edit Routing Rules")
