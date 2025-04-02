import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Cvent Integration - Verathon",
    page_icon="🔄",
    layout="wide"
)

# Header
st.title("Cvent Integration & Management")
st.markdown("Manage your Cvent integration and optimize webinar marketing")

# Integration Status Dashboard
st.header("Integration Status")
status_col1, status_col2, status_col3, status_col4 = st.columns(4)

with status_col1:
    st.metric(
        label="Connection Status",
        value="Connected",
        delta="Stable"
    )

with status_col2:
    st.metric(
        label="Last Sync",
        value="Today, 09:45 AM",
        delta="2 hours ago"
    )

with status_col3:
    st.metric(
        label="Events Synchronized",
        value="24",
        delta="+3"
    )

with status_col4:
    st.metric(
        label="Data Quality Score",
        value="92%",
        delta="+5%"
    )

# Crawl-Walk-Run Framework for Cvent
st.header("Crawl-Walk-Run Framework for Cvent")
cvent_tabs = st.tabs(["Crawl Stage", "Walk Stage", "Run Stage"])

with cvent_tabs[0]:
    st.subheader("Crawl Stage: Fundamental Integration")
    
    crawl_col1, crawl_col2 = st.columns(2)
    
    with crawl_col1:
        st.markdown("""
        ### Implementation Focus:
        
        1. **Basic API Connection**
           - One-way data sync from Cvent to marketing platform
           - Manual event creation and management
           - Basic registration data capture
        
        2. **Essential Webinar Elements**
           - Standard registration forms
           - Basic email confirmations
           - Simple post-event follow-up emails
           - Manual reporting and data exports
        
        3. **Team Requirements**
           - Cvent administrator (part-time)
           - Marketing coordinator for webinar setup
           - Manual lead processing
        """)
    
    with crawl_col2:
        # Implementation checklist
        st.subheader("Implementation Checklist")
        
        crawl_items = {
            "API Configuration": True,
            "Authentication Setup": True,
            "Event Template Creation": True,
            "Registration Form Setup": True,
            "Email Template Configuration": True,
            "Basic Reporting Setup": True,
            "Test Event Configuration": True,
            "Team Training Completed": False,
            "Documentation Created": False
        }
        
        for item, completed in crawl_items.items():
            if completed:
                st.success(f"✅ {item}")
            else:
                st.error(f"❌ {item}")
                
        # Progress indicator
        crawl_progress = sum(crawl_items.values()) / len(crawl_items) * 100
        
        st.progress(crawl_progress / 100)
        st.info(f"Crawl Stage Implementation: {crawl_progress:.1f}% Complete")

with cvent_tabs[1]:
    st.subheader("Walk Stage: Enhanced Integration")
    
    walk_col1, walk_col2 = st.columns(2)
    
    with walk_col1:
        st.markdown("""
        ### Implementation Focus:
        
        1. **Advanced Data Exchange**
           - Bi-directional sync between Cvent and marketing platforms
           - Automated event creation from templates
           - Enhanced participant data collection
           - Custom field mapping between systems
        
        2. **Enhanced Webinar Capabilities**
           - Segmented registration pathways
           - Personalized email journeys
           - Interactive webinar elements
           - Automated attendee follow-up
           - Integrated performance reporting
        
        3. **Team Configuration**
           - Dedicated Cvent administrator
           - Webinar program manager
           - Automated lead routing workflows
        """)
    
    with walk_col2:
        # Implementation readiness assessment
        st.subheader("Walk Stage Readiness Assessment")
        
        walk_readiness = {
            "Crawl Stage Completed": 85,
            "Marketing Automation Integration": 60,
            "CRM Integration Readiness": 70,
            "Custom Field Mapping": 50,
            "Team Training Level": 65,
            "Webinar Process Documentation": 55,
            "Data Quality Management": 60
        }
        
        # Create horizontal bar chart for readiness assessment
        walk_df = pd.DataFrame({
            'Area': list(walk_readiness.keys()),
            'Readiness': list(walk_readiness.values())
        })
        
        fig = px.bar(
            walk_df,
            x='Readiness',
            y='Area',
            orientation='h',
            title="Walk Stage Readiness Assessment",
            color='Readiness',
            color_continuous_scale=px.colors.sequential.Viridis,
            range_color=[0, 100]
        )
        
        fig.add_vline(x=75, line_dash="dash", line_color="red", annotation_text="Required for Walk Stage")
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Overall readiness
        avg_readiness = sum(walk_readiness.values()) / len(walk_readiness)
        st.info(f"Overall Walk Stage Readiness: {avg_readiness:.1f}%")
        
        if avg_readiness < 75:
            st.warning("⚠️ Additional preparation needed before advancing to Walk Stage")
        else:
            st.success("✅ Ready to implement Walk Stage capabilities")

with cvent_tabs[2]:
    st.subheader("Run Stage: Advanced Integration")
    
    run_col1, run_col2 = st.columns(2)
    
    with run_col1:
        st.markdown("""
        ### Implementation Focus:
        
        1. **Comprehensive System Integration**
           - Full API utilization and custom integration
           - Real-time data synchronization
           - Advanced event management automation
           - Predictive analytics implementation
        
        2. **Advanced Webinar Program**
           - AI-powered personalization
           - Dynamic content delivery
           - Behavior-based engagement tactics
           - Comprehensive ROI tracking
           - Multi-channel integrated promotion
        
        3. **Team Evolution**
           - Strategic webinar program director
           - Cross-functional integrated team
           - AI-assisted webinar optimization
        """)
    
    with run_col2:
        # Prerequisites for Run stage
        st.subheader("Run Stage Prerequisites")
        
        st.markdown("""
        **Key Milestones Required:**
        
        1. ✅ Walk stage fully implemented and operational for 3+ months
        2. ⚠️ Data quality score consistently above 90%
        3. ❌ Integration uptime exceeding 99.5%
        4. ⚠️ Team certified on advanced Cvent features
        5. ❌ Marketing automation workflows fully implemented
        6. ✅ CRM bidirectional sync established
        7. ❌ ROI tracking framework deployed
        
        **Current Status:** Not Ready for Run Stage
        
        **Estimated Timeline:** Q3 2024 readiness based on current progress
        """)
        
        # Run stage roadmap visualization
        roadmap_data = pd.DataFrame({
            'Task': [
                'Complete Walk Stage Implementation',
                'Data Quality Improvement Program',
                'Advanced Team Training',
                'Marketing Automation Enhancement',
                'Analytics Framework Development',
                'AI Implementation Planning',
                'Run Stage Deployment'
            ],
            'Start': ['2023-12-01', '2024-01-15', '2024-02-01', '2024-03-01', '2024-04-15', '2024-06-01', '2024-07-15'],
            'End': ['2024-02-28', '2024-03-30', '2024-04-15', '2024-05-30', '2024-06-30', '2024-07-30', '2024-09-30'],
            'Status': ['In Progress', 'Not Started', 'Not Started', 'Not Started', 'Not Started', 'Not Started', 'Not Started']
        })
        
        # Convert to datetime for plotting
        roadmap_data['Start'] = pd.to_datetime(roadmap_data['Start'])
        roadmap_data['End'] = pd.to_datetime(roadmap_data['End'])
        
        # Add a color mapping for status
        status_colors = {
            'Completed': 'green',
            'In Progress': 'blue',
            'Not Started': 'gray'
        }
        roadmap_data['Color'] = roadmap_data['Status'].map(status_colors)
        
        fig = px.timeline(
            roadmap_data,
            x_start='Start',
            x_end='End',
            y='Task',
            color='Status',
            title="Run Stage Implementation Roadmap"
        )
        
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True)

# Cvent Data Management
st.header("Cvent Data Management")
data_tabs = st.tabs(["Event Data", "Registration Data", "Attendee Data"])

with data_tabs[0]:
    # Event data sample
    st.subheader("Event Data Sync Status")
    
    event_data = pd.DataFrame({
        'Event ID': ['EVT001', 'EVT002', 'EVT003', 'EVT004', 'EVT005', 'EVT006'],
        'Event Name': [
            'Product A Clinical Applications', 
            'Healthcare Innovation Summit', 
            'Visualization Technology Webinar',
            'Q2 Product Roadmap Update',
            'Hospital Efficiency Workshop',
            'New Feature Introduction'
        ],
        'Event Date': ['2023-12-15', '2024-01-20', '2024-02-12', '2024-03-05', '2024-03-22', '2024-04-10'],
        'Event Type': ['Webinar', 'Virtual Conference', 'Webinar', 'Webinar', 'Workshop', 'Webinar'],
        'Status': ['Active', 'Planning', 'Planning', 'Draft', 'Planning', 'Draft'],
        'Sync Status': ['Synced', 'Synced', 'Synced', 'Pending', 'Synced', 'Error']
    })
    
    # Style the dataframe with colors for sync status
    def highlight_sync_status(val):
        if val == 'Synced':
            return 'background-color: #d4f1de'
        elif val == 'Pending':
            return 'background-color: #fff2cc'
        elif val == 'Error':
            return 'background-color: #ffd9d9'
        return ''
    
    # Display styled dataframe
    st.dataframe(event_data.style.applymap(highlight_sync_status, subset=['Sync Status']), use_container_width=True)
    
    # Sync status summary
    sync_summary = pd.DataFrame({
        'Status': ['Synced', 'Pending', 'Error'],
        'Count': [4, 1, 1]
    })
    
    fig = px.pie(
        sync_summary,
        values='Count',
        names='Status',
        title="Event Sync Status Distribution",
        color='Status',
        color_discrete_map={'Synced': '#88c999', 'Pending': '#ffda73', 'Error': '#ff8080'}
    )
    st.plotly_chart(fig, use_container_width=True)

with data_tabs[1]:
    # Registration data
    st.subheader("Registration Data Management")
    
    # Registration form fields mapping
    st.markdown("### Registration Form Field Mapping")
    
    field_mapping = pd.DataFrame({
        'Cvent Field': [
            'First Name', 
            'Last Name', 
            'Email Address', 
            'Company Name',
            'Job Title',
            'Phone Number',
            'Industry',
            'Country',
            'Product Interest',
            'Registration Date'
        ],
        'Marketing Platform Field': [
            'FirstName', 
            'LastName', 
            'EmailAddress', 
            'Company',
            'Title',
            'Phone',
            'Industry',
            'Country',
            'ProductInterest',
            'RegistrationDate'
        ],
        'CRM Field': [
            'First_Name__c', 
            'Last_Name__c', 
            'Email__c', 
            'Company_Name__c',
            'Title__c',
            'Phone__c',
            'Industry__c',
            'Country__c',
            'Product_Interest__c',
            'Registration_Date__c'
        ],
        'Mapping Status': [
            'Mapped', 
            'Mapped', 
            'Mapped', 
            'Mapped',
            'Mapped',
            'Mapped',
            'Mapped',
            'Mapped',
            'Custom Mapping',
            'Mapped'
        ]
    })
    
    st.dataframe(field_mapping, use_container_width=True)
    
    # Registration form templates
    st.markdown("### Registration Form Templates")
    
    form_col1, form_col2, form_col3 = st.columns(3)
    
    with form_col1:
        st.info("**Standard Webinar Registration**")
        st.markdown("""
        - Basic contact information
        - Company details
        - Product interest (single select)
        - Privacy policy consent
        - Marketing opt-in
        """)
        st.button("Edit Template", key="edit_standard")

    with form_col2:
        st.info("**Advanced Webinar Registration**")
        st.markdown("""
        - Extended contact details
        - Role & purchasing authority
        - Product interest (multi-select)
        - Custom questions (3 max)
        - Privacy & marketing consents
        """)
        st.button("Edit Template", key="edit_advanced")

    with form_col3:
        st.info("**Conference Registration**")
        st.markdown("""
        - Full contact profile
        - Session selection
        - Dietary preferences
        - Multiple custom questions
        - Document uploads
        - Payment processing
        """)
        st.button("Edit Template", key="edit_conference")

with data_tabs[2]:
    # Attendee data
    st.subheader("Attendee Data & Engagement Metrics")
    
    # Sample attendee data with engagement metrics
    st.markdown("### Sample Attendee Engagement Data")
    
    attendee_data = pd.DataFrame({
        'Attendee ID': ['ATT001', 'ATT002', 'ATT003', 'ATT004', 'ATT005'],
        'Event': ['Product A Clinical Applications', 'Product A Clinical Applications', 'Product A Clinical Applications', 'Product A Clinical Applications', 'Product A Clinical Applications'],
        'Attendance Duration': [45, 55, 32, 58, 20],
        'Questions Asked': [2, 1, 0, 3, 0],
        'Poll Responses': [4, 5, 2, 5, 1],
        'Resources Downloaded': [3, 2, 1, 4, 0],
        'Engagement Score': [85, 90, 60, 95, 40]
    })
    
    # Function to color engagement score
    def color_engagement_score(val):
        if val >= 80:
            return 'background-color: #d4f1de'
        elif val >= 60:
            return 'background-color: #fff2cc'
        else:
            return 'background-color: #ffd9d9'
    
    # Display styled dataframe
    st.dataframe(attendee_data.style.applymap(color_engagement_score, subset=['Engagement Score']), use_container_width=True)
    
    # Engagement distribution
    engagement_col1, engagement_col2 = st.columns(2)
    
    with engagement_col1:
        # Create engagement score distribution
        engagement_bins = pd.cut(attendee_data['Engagement Score'], bins=[0, 40, 60, 80, 100], labels=['Very Low', 'Low', 'Medium', 'High'])
        engagement_counts = engagement_bins.value_counts().reset_index()
        engagement_counts.columns = ['Engagement Level', 'Count']
        
        fig = px.bar(
            engagement_counts,
            x='Engagement Level',
            y='Count',
            title="Attendee Engagement Distribution",
            color='Engagement Level',
            color_discrete_map={
                'High': '#88c999',
                'Medium': '#ffda73',
                'Low': '#ff8080',
                'Very Low': '#ff5252'
            }
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with engagement_col2:
        # Engagement metrics correlation
        fig = px.scatter(
            attendee_data,
            x='Attendance Duration',
            y='Engagement Score',
            size='Questions Asked',
            color='Resources Downloaded',
            title="Engagement Metrics Correlation"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Post-webinar workflow
    st.subheader("Post-Webinar Automated Workflows")
    
    st.markdown("""
    ### Engagement-Based Follow-up Rules:
    
    | Engagement Level | Follow-up Action | Timing | Owner |
    | --- | --- | --- | --- |
    | High (80-100) | Direct sales outreach + resources | Within 24 hours | Sales rep |
    | Medium (60-79) | Personalized email + targeted content | Within 48 hours | Marketing automation |
    | Low (40-59) | Educational nurture sequence | Within 72 hours | Marketing automation |
    | Very Low (<40) | Re-engagement campaign | Within 1 week | Marketing automation |
    """)
    
    st.button("Edit Follow-up Rules")

# Cvent API & Integration Settings
st.header("Cvent API Configuration")

api_col1, api_col2 = st.columns(2)

with api_col1:
    st.subheader("API Connection Settings")
    
    st.text_input("API Endpoint URL", value="https://api.cvent.com/v1")
    api_key = st.text_input("API Key", value="************", type="password")
    
    st.selectbox("Authentication Method", ["OAuth 2.0", "API Key", "JWT"])
    
    st.selectbox("Environment", ["Production", "Sandbox"])
    
    st.number_input("Request Timeout (seconds)", min_value=5, max_value=60, value=30)
    
    st.selectbox("Logging Level", ["Error", "Warning", "Info", "Debug"])
    
    sync_col1, sync_col2 = st.columns(2)
    with sync_col1:
        st.button("Test Connection")
    with sync_col2:
        st.button("Save Settings")

with api_col2:
    st.subheader("Data Sync Configuration")
    
    st.selectbox("Sync Frequency", ["Real-time", "Every 15 minutes", "Hourly", "Daily", "Custom"])
    
    st.multiselect(
        "Data to Sync", 
        ["Events", "Registrations", "Attendees", "Sessions", "Speakers", "Questions", "Polls", "Resources", "Engagement Metrics"],
        default=["Events", "Registrations", "Attendees", "Engagement Metrics"]
    )
    
    st.checkbox("Enable Bidirectional Sync", value=True)
    
    st.checkbox("Auto-resolve Conflicts", value=True)
    
    st.checkbox("Sync Historical Data", value=False)
    
    if st.checkbox("Advanced Settings", value=False):
        st.number_input("Maximum Records per Sync", min_value=100, max_value=10000, value=1000)
        st.text_area("Custom Filters", height=100)
        st.text_area("Error Handling Instructions", height=100)
    
    sync_col1, sync_col2 = st.columns(2)
    with sync_col1:
        st.button("Manual Sync Now")
    with sync_col2:
        st.button("View Sync Logs")

# Support & Resources
st.header("Support & Resources")
resource_col1, resource_col2, resource_col3 = st.columns(3)

with resource_col1:
    st.subheader("Cvent Documentation")
    st.markdown("""
    - [Cvent API Documentation](https://developer.cvent.com/)
    - [Best Practices Guide](https://www.cvent.com/en/resources)
    - [Webinar Setup Tutorial](https://www.cvent.com/en/resources)
    - [Data Management Guide](https://www.cvent.com/en/resources)
    - [Advanced Reporting Guide](https://www.cvent.com/en/resources)
    """)

with resource_col2:
    st.subheader("Integration Support")
    st.markdown("""
    - [Troubleshooting Guide](https://support.digitalfactory24.com)
    - [Common Integration Issues](https://support.digitalfactory24.com)
    - [Sync Error Resolution](https://support.digitalfactory24.com)
    - [Performance Optimization Tips](https://support.digitalfactory24.com)
    - [Contact Support Team](mailto:support@digitalfactory24.com)
    """)

with resource_col3:
    st.subheader("Training Resources")
    st.markdown("""
    - [Video Tutorials Library](https://training.digitalfactory24.com)
    - [Admin Certification Path](https://training.digitalfactory24.com)
    - [Webinar Best Practices](https://training.digitalfactory24.com)
    - [Data Analysis Workshop](https://training.digitalfactory24.com)
    - [Monthly Webinar Series](https://training.digitalfactory24.com)
    """)
