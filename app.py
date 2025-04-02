import streamlit as st
from PIL import Image
import os
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Verathon Marketing Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Verathon brand colors
VERATHON_BLUE = "#0056A7"
VERATHON_WHITE = "#FFFFFF"
DF24_PRIMARY = "#008080"  # Digital Factory 24 primary color

# Main title with Verathon branding
st.markdown(f'<h1 style="color:{VERATHON_BLUE};">Verathon Marketing Intelligence Platform</h1>', unsafe_allow_html=True)
st.markdown(f'<h3 style="color:{VERATHON_BLUE};">Powered by Digital Factory 24</h3>', unsafe_allow_html=True)

# Introduction
st.markdown("""
## Comprehensive Digital & Webinar Marketing Management

This platform provides Verathon with an integrated solution for managing digital marketing campaigns, 
webinar programs, and competitive intelligence in real-time, with a focus on your new product line launch.

### Key Features:
- **Digital Marketing Dashboard**: Track KPIs and campaign performance with advanced GTM integrations
- **Campaign & Tag Management**: Centralized control of all digital marketing tags and campaigns
- **Webinar Management Framework**: Implement the Crawl-Walk-Run methodology with Cvent integration
- **Competitive Intelligence**: Real-time research and market insights with gap analysis
- **Marketing Automation**: Workflow creation and management with 24/7 support
- **ROI Analytics**: Track and optimize marketing investments for faster time-to-value
- **Product Launch Analytics**: Specialized analytics for new product line introduction
""")

# Digital Factory 24 Framework visualization
st.header("Digital Factory 24's Growth Maturity Framework")

# Create a 3D-style diagram for the framework stages
framework_data = pd.DataFrame({
    'Stage': ['Foundation', 'Development', 'Expansion', 'Innovation', 'Sustaining Success'],
    'Level': [1, 2, 3, 4, 5],
    'Value': [85, 70, 60, 45, 30],  # Size of the circles
    'Description': [
        'Building the Basics',
        'Enhancing Engagement',
        'Scaling for Success',
        'Leading the Market',
        'Continuous Optimization'
    ]
})

fig = px.scatter(
    framework_data,
    x='Level',
    y='Value',
    size='Value',
    text='Stage',
    color='Stage',
    color_discrete_sequence=[VERATHON_BLUE, "#3C78D8", "#6FA8DC", "#9FC5E8", "#CFE2F3"],
    size_max=60,
    height=400
)

# Customize to look more 3D-like
fig.update_traces(
    textposition='middle center',
    textfont=dict(color='white', size=12),
    marker=dict(opacity=0.9, line=dict(width=2, color='white')),
)

# Add connecting lines to show progression
fig.add_trace(
    go.Scatter(
        x=framework_data['Level'],
        y=framework_data['Value'],
        mode='lines',
        line=dict(color=VERATHON_BLUE, width=3),
        showlegend=False
    )
)

# Clean up the layout
fig.update_layout(
    title="Digital Marketing Growth Maturity Journey",
    xaxis_title="",
    yaxis_title="",
    xaxis=dict(showticklabels=False, showgrid=False),
    yaxis=dict(showticklabels=False, showgrid=False),
    plot_bgcolor='rgba(0,0,0,0)',
)

st.plotly_chart(fig, use_container_width=True)

# Add descriptions under the chart
framework_cols = st.columns(5)

with framework_cols[0]:
    st.markdown(f"**Foundation Stage**")
    st.markdown("- SEO & Content Strategy")
    st.markdown("- UI/UX Design Basics")
    st.markdown("- Initial Campaign Setup")

with framework_cols[1]:
    st.markdown(f"**Development Stage**")
    st.markdown("- Enhanced Campaigns")
    st.markdown("- Audience Segmentation")
    st.markdown("- Data-Driven Decisions")

with framework_cols[2]:
    st.markdown(f"**Expansion Stage**")
    st.markdown("- Multi-channel Integration")
    st.markdown("- Advanced Analytics")
    st.markdown("- Personalization")

with framework_cols[3]:
    st.markdown(f"**Innovation Stage**")
    st.markdown("- AI-Powered Marketing")
    st.markdown("- Predictive Analytics")
    st.markdown("- MarTech Innovations")

with framework_cols[4]:
    st.markdown(f"**Sustaining Success**")
    st.markdown("- Continuous Optimization")
    st.markdown("- Market Trend Adaptation")
    st.markdown("- Future-Proof Strategy")

# Dashboard sections with image previews
st.markdown("---")
st.header("Platform Capabilities")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Digital Marketing & Campaign Analytics")
    st.image("https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a", 
             caption="Advanced Campaign Analytics Dashboard")
    st.markdown("""
    Track all your digital marketing KPIs with Google Tag Manager integration, providing real-time insights 
    and alerts. Digital Factory 24 specializes in GTM implementation and campaign analytics with a 24/7 
    support team ready to optimize your marketing performance.
    
    **Key Benefits:**
    - Centralized tag management across all digital properties
    - Automated tracking implementation for new product launches
    - Custom attribution models for accurate ROI measurement
    - 24/7 support for campaign optimization
    """)
    st.button("Explore Digital Analytics", key="dashboard_btn")

with col2:
    st.subheader("Webinar Marketing Framework")
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4", 
             caption="Webinar Management System with Cvent Integration")
    st.markdown("""
    Manage your webinar program using the Crawl-Walk-Run framework, with seamless Cvent integration. 
    Digital Factory 24's webinar experts provide end-to-end management, from registration optimization 
    to post-event lead nurturing.
    
    **Key Benefits:**
    - Optimized registration pathways increasing conversion by 35%
    - Engagement strategies driving 40% higher attendance rates
    - Automated post-event workflows for faster lead processing
    - Comprehensive analytics for continuous improvement
    """)
    st.button("Explore Webinar Management", key="webinar_btn")

# New product launch section
st.markdown("---")
st.header("New Product Launch Acceleration")

new_product_col1, new_product_col2 = st.columns([1, 1])

with new_product_col1:
    st.markdown(f"""
    ### Accelerating Time-to-Market for Verathon's New Product Line
    
    Digital Factory 24 provides a comprehensive GTM acceleration program specifically designed for Verathon's 
    new product introduction. Our approach combines market intelligence, digital campaign strategies, and 
    conversion optimization to drive faster market adoption and ROI.
    
    **Our integrated approach delivers:**
    - **30% faster** time-to-market compared to traditional launch approaches
    - **40% increase** in qualified leads during the critical launch phase
    - **25% higher** conversion rates through optimized digital journeys
    - **Real-time market feedback** for agile strategy adjustments
    """)
    
    st.button("View New Product GTM Playbook", key="gtm_btn")

with new_product_col2:
    # Create a simple funnel chart showing accelerated GTM process
    funnel_stages = ['Market Research', 'Strategy Development', 'Campaign Creation', 'Launch Execution', 'Performance Optimization']
    traditional_values = [100, 80, 65, 50, 35]
    df24_values = [100, 95, 85, 75, 60]
    
    fig = go.Figure()
    
    fig.add_trace(go.Funnel(
        name = 'Traditional Approach',
        y = funnel_stages,
        x = traditional_values,
        textinfo = "value+percent initial",
        marker = {"color": "lightgrey"}
    ))
    
    fig.add_trace(go.Funnel(
        name = 'DF24 Accelerated Approach',
        y = funnel_stages,
        x = df24_values,
        textinfo = "value+percent initial",
        marker = {"color": VERATHON_BLUE}
    ))
    
    fig.update_layout(
        title="GTM Acceleration Comparison",
        height=400,
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Case studies section
st.markdown("---")
st.header("Industry Success Stories")

tabs = st.tabs(["Healthcare", "Medical Devices", "Technology", "Pharmaceuticals"])

with tabs[0]:
    healthcare_col1, healthcare_col2 = st.columns([2, 1])
    
    with healthcare_col1:
        st.subheader("Leading Healthcare Provider")
        st.markdown("""
        **Challenge:** A major healthcare provider struggled with digital campaign effectiveness and measuring ROI 
        across multiple service lines.
        
        **Solution:** Digital Factory 24 implemented an integrated GTM strategy with:
        - Unified campaign tracking architecture using GTM
        - Advanced segmentation model based on service line interest
        - Personalized nurture journeys for each patient segment
        - Real-time ROI dashboard for marketing leadership
        
        **Results:**
        - 42% increase in qualified patient leads
        - 28% reduction in cost-per-acquisition
        - 167% improvement in campaign ROI
        - Complete visibility into marketing performance
        """)
    
    with healthcare_col2:
        # Create a bar chart showing the results
        results_data = pd.DataFrame({
            'Metric': ['Lead Increase', 'CPA Reduction', 'ROI Improvement'],
            'Percentage': [42, 28, 167]
        })
        
        fig = px.bar(
            results_data, 
            x='Percentage', 
            y='Metric', 
            orientation='h',
            color='Percentage',
            color_continuous_scale=['#0056A7', '#4682B4', '#87CEEB'],
            labels={'Percentage': 'Improvement (%)'},
            title="Healthcare Case Study Results"
        )
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

with tabs[1]:
    medical_col1, medical_col2 = st.columns([2, 1])
    
    with medical_col1:
        st.subheader("Global Medical Device Manufacturer")
        st.markdown("""
        **Challenge:** A medical device company needed to launch a new product line with limited marketing resources 
        and tight timelines.
        
        **Solution:** Digital Factory 24 deployed a rapid-launch GTM program:
        - Comprehensive competitive intelligence for positioning
        - Integrated digital campaign with specialized landing pages
        - Webinar series targeting key decision-makers
        - Sales enablement portal with real-time lead intelligence
        
        **Results:**
        - Product launch accelerated by 45 days
        - 52% higher lead generation than previous launches
        - 35% increase in sales team engagement
        - 3.2X ROI within first 6 months
        """)
    
    with medical_col2:
        # Create a timeline chart showing the accelerated launch
        timeline_data = pd.DataFrame({
            'Stage': ['Planning', 'Development', 'Testing', 'Launch', 'Optimization'],
            'Traditional': [30, 45, 30, 15, 30],
            'DF24 Approach': [20, 25, 15, 10, 15]
        })
        
        timeline_data['Traditional_Cumulative'] = timeline_data['Traditional'].cumsum()
        timeline_data['DF24_Cumulative'] = timeline_data['DF24 Approach'].cumsum()
        
        fig = px.line(
            timeline_data, 
            x='Stage', 
            y=['Traditional_Cumulative', 'DF24_Cumulative'],
            markers=True,
            labels={'value': 'Days', 'variable': 'Approach'},
            title="Launch Timeline Comparison",
            color_discrete_map={
                'Traditional_Cumulative': 'lightgrey',
                'DF24_Cumulative': VERATHON_BLUE
            }
        )
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

with tabs[2]:
    st.subheader("Enterprise Technology Provider")
    st.markdown("""
    **Challenge:** A technology company struggled with tracking customer journey across complex product offerings 
    and needed to improve lead quality for sales.
    
    **Solution:** Digital Factory 24 implemented comprehensive solution:
    - Cross-domain tracking architecture with unified analytics
    - Advanced lead scoring model based on behavioral data
    - Custom attribution modeling for complex purchase journeys
    - Integrated CRM workflows for sales enablement
    
    **Results:**
    - 63% improvement in marketing qualified lead accuracy
    - 47% increase in lead-to-opportunity conversion
    - 55% reduction in sales cycle length
    - 2.8X increase in marketing-attributed revenue
    """)

with tabs[3]:
    st.subheader("Pharmaceutical Company")
    st.markdown("""
    **Challenge:** A pharmaceutical firm needed to educate healthcare professionals about a new therapy while 
    maintaining compliance with industry regulations.
    
    **Solution:** Digital Factory 24 created a compliant digital strategy:
    - Regulatory-approved content workflow
    - HCP-targeted webinar series with verification
    - Secure content portal with engagement tracking
    - Closed-loop reporting for compliance documentation
    
    **Results:**
    - 87% engagement rate among target HCP audience
    - 45% increase in therapy awareness
    - 38% reduction in education cost per HCP
    - Full compliance with all regulatory requirements
    """)

# Competitive spectrum mapping
st.markdown("---")
st.header("Competitive Intelligence: Market Position Analysis")

# Create data for the competitive positioning chart
competitors = ['Verathon', 'Competitor A', 'Competitor B', 'Competitor C', 'Competitor D']
dimensions = ['Digital Presence', 'GTM Effectiveness', 'Campaign Integration', 'Technology Adoption', 'Customer Experience']

# Create random scores for demonstration (1-10 scale)
np.random.seed(42)  # For reproducibility
competitor_data = {}

# Verathon scores - slightly above average but with room for improvement
competitor_data['Verathon'] = [7, 6, 5, 6, 7]

# Generate scores for competitors
competitor_data['Competitor A'] = [8, 7, 9, 8, 7]
competitor_data['Competitor B'] = [6, 8, 7, 9, 8]
competitor_data['Competitor C'] = [5, 4, 6, 7, 5]
competitor_data['Competitor D'] = [7, 6, 5, 4, 6]

# Create the radar chart
fig = go.Figure()

for competitor in competitors:
    fig.add_trace(go.Scatterpolar(
        r=competitor_data[competitor],
        theta=dimensions,
        fill='toself',
        name=competitor,
        opacity=0.8
    ))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10]
        )),
    showlegend=True,
    title="Competitive Digital Marketing Capabilities",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

comp_col1, comp_col2 = st.columns(2)

with comp_col1:
    st.subheader("Competitive Gap Analysis")
    st.markdown("""
    Our analysis reveals several key areas where Digital Factory 24 can help Verathon gain competitive advantage:
    
    1. **GTM Acceleration** - Competitors A and B have more mature GTM processes, but our accelerated framework can close this gap within 90 days
    
    2. **Campaign Integration** - Most competitors are struggling with true cross-channel integration; our unified approach provides immediate differentiation
    
    3. **Technology Adoption** - While Competitor B leads in technology, their implementation lacks strategic alignment; our approach combines technology with strategic execution
    
    4. **Digital Experience** - All competitors score lower on customer experience metrics; our UX/UI expertise can create a significant competitive advantage
    """)

with comp_col2:
    st.subheader("Digital Factory 24 Advantage")
    st.markdown("""
    Working with Digital Factory 24 provides Verathon with unique advantages:
    
    ✓ **24/7 Expert Support** - Our global team ensures continuous optimization and immediate response to market changes
    
    ✓ **Award-Winning UX/UI Team** - Our design specialists create intuitive, engaging digital experiences that drive conversion
    
    ✓ **GTM Specialization** - Deep expertise in accelerating product launches across medical and healthcare verticals
    
    ✓ **Campaign & Tag Management** - Specialized knowledge in creating coherent tracking architecture and campaign measurement
    
    ✓ **Proven Results** - Consistent track record of delivering 25%+ improvements in digital marketing ROI
    """)

# Digital Factory 24's unique UX/UI capabilities
st.markdown("---")
st.header("Digital Factory 24's UX/UI Excellence")

ux_col1, ux_col2 = st.columns([2, 1])

with ux_col1:
    st.markdown("""
    ### Transforming User Experience for Verathon
    
    Digital Factory 24's UX/UI team brings world-class design expertise to elevate Verathon's digital presence 
    and create exceptional customer experiences across all touchpoints.
    
    **Our UX/UI approach delivers:**
    - **User-Centered Design** - Research-driven experiences tailored to your specific audience needs
    - **Conversion Optimization** - Strategic design elements that guide users toward desired actions
    - **Brand Consistency** - Unified visual language across all digital touchpoints
    - **Accessibility Standards** - Inclusive design practices ensuring all users can engage effectively
    - **Mobile-First Approach** - Optimized experiences across all devices and screen sizes
    
    Our team has transformed digital experiences for leading healthcare and medical device companies, delivering 
    average conversion improvements of 40% through strategic UX/UI enhancements.
    """)

with ux_col2:
    # Create a stacked bar chart showing UX improvement results
    ux_data = pd.DataFrame({
        'Metric': ['Conversion Rate', 'Engagement Time', 'Task Completion', 'User Satisfaction'],
        'Before': [20, 45, 65, 72],
        'After': [42, 72, 89, 94]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=ux_data['Metric'],
        y=ux_data['Before'],
        name='Before DF24',
        marker_color='lightgrey'
    ))
    
    fig.add_trace(go.Bar(
        x=ux_data['Metric'],
        y=ux_data['After'] - ux_data['Before'],  # Show only the improvement
        name='DF24 Improvement',
        marker_color=VERATHON_BLUE,
        base=ux_data['Before']  # Start from the "before" value
    ))
    
    fig.update_layout(
        title="UX/UI Improvement Impact",
        yaxis_title="Percentage (%)",
        barmode='stack',
        height=300
    )
    
    st.plotly_chart(fig, use_container_width=True)

# 24/7 Support Model
st.markdown("---")
st.header("24/7 Global Support & Expertise")

support_col1, support_col2, support_col3 = st.columns(3)

with support_col1:
    st.markdown("""
    ### Always-On Campaign Management
    
    Digital Factory 24's global team provides around-the-clock campaign monitoring and optimization, ensuring 
    your marketing efforts never miss an opportunity.
    
    - Real-time performance monitoring
    - Immediate anomaly detection and resolution
    - Continuous A/B testing and optimization
    - Performance updates every morning
    """)

with support_col2:
    st.markdown("""
    ### Strategic Data Analysis
    
    Our analytics team works across time zones to transform your marketing data into actionable insights 
    and strategic recommendations.
    
    - Overnight data processing and analysis
    - Morning strategy recommendations
    - Continuous competitive monitoring
    - Weekly insight reports and strategy adjustments
    """)

with support_col3:
    st.markdown("""
    ### Technical Excellence
    
    Technical implementation and troubleshooting available 24/7, ensuring your marketing technology 
    ecosystem operates flawlessly.
    
    - GTM and tracking implementation
    - Integration maintenance and optimization
    - Emergency technical support
    - Continuous performance optimization
    """)

# World map showing global support
support_locations = pd.DataFrame({
    'city': ['New York', 'London', 'Singapore', 'Sydney', 'Tokyo', 'Berlin', 'Mumbai', 'San Francisco'],
    'lat': [40.7128, 51.5074, 1.3521, -33.8688, 35.6762, 52.5200, 19.0760, 37.7749],
    'lon': [-74.0060, -0.1278, 103.8198, 151.2093, 139.6503, 13.4050, 72.8777, -122.4194],
    'size': [25, 20, 15, 15, 10, 15, 20, 25]
})

fig = px.scatter_geo(
    support_locations,
    lat='lat',
    lon='lon',
    size='size',
    color_discrete_sequence=[VERATHON_BLUE],
    projection='natural earth',
    title="Digital Factory 24 Global Support Centers",
    height=400
)

fig.update_geos(
    showcountries=True,
    countrycolor="Gray",
    showcoastlines=True,
    coastlinecolor="Gray",
    showland=True,
    landcolor="lightgray",
    showocean=True,
    oceancolor="aliceblue"
)

fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))

st.plotly_chart(fig, use_container_width=True)

# Footer with resources
st.markdown("---")
st.subheader("Resources & Documentation")

resources_col1, resources_col2, resources_col3, resources_col4 = st.columns(4)

with resources_col1:
    st.markdown("**Getting Started Guide**")
    st.markdown("- Platform overview")
    st.markdown("- Setting up your first dashboard")
    st.markdown("- Integrating with Cvent")
    st.markdown("- GTM implementation guide")

with resources_col2:
    st.markdown("**Marketing Templates**")
    st.markdown("- Campaign workflow templates")
    st.markdown("- KPI report templates")
    st.markdown("- Webinar marketing checklist")
    st.markdown("- Product launch playbook")

with resources_col3:
    st.markdown("**Technology Resources**")
    st.markdown("- Google Tag Manager setup")
    st.markdown("- Campaign tracking guide")
    st.markdown("- Analytics implementation")
    st.markdown("- Marketing automation flows")

with resources_col4:
    st.markdown("**Support & Services**")
    st.markdown("- 24/7 support access")
    st.markdown("- UX/UI consultation")
    st.markdown("- Strategy workshops")
    st.markdown("- Training resources")

# Final CTA
st.markdown("---")
st.markdown(f"""
<div style="background-color:{VERATHON_BLUE}; padding:15px; border-radius:5px; text-align:center;">
    <h2 style="color:white;">Ready to accelerate your marketing success?</h2>
    <p style="color:white;">Contact your Digital Factory 24 representative to get started with a customized implementation plan.</p>
</div>
""", unsafe_allow_html=True)

# Add copyright footer
st.markdown("")
st.markdown("<p style='text-align:center; color:gray; font-size:12px;'>© 2024 Digital Factory 24. Created exclusively for Verathon.</p>", unsafe_allow_html=True)
