import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Tag Management System - Verathon",
    page_icon="🏷️",
    layout="wide"
)

# Verathon brand colors
VERATHON_BLUE = "#0056A7"
VERATHON_WHITE = "#FFFFFF"

# Header
st.markdown(f'<h1 style="color:{VERATHON_BLUE};">Tag Management System</h1>', unsafe_allow_html=True)
st.markdown("Unified campaign tracking and analytics through Google Tag Manager expertise")

# Key challenges section
st.header("Addressing Verathon's Tag Management Challenges")

challenges_col1, challenges_col2 = st.columns(2)

with challenges_col1:
    st.markdown("""
    ### Current Challenges
    
    Our analysis has identified several key challenges in Verathon's current campaign and tag management approach:
    
    1. **Fragmented Tag Implementation** - Different tags across various properties creating inconsistent data collection
    
    2. **Limited Cross-Domain Tracking** - Inability to track user journeys across multiple web properties
    
    3. **Manual Campaign Setup** - Time-consuming process for launching new campaigns, especially for new product lines
    
    4. **Data Silos** - Marketing data isolated from sales and product data, preventing unified analysis
    
    5. **Complex Attribution** - Limited visibility into which marketing touchpoints drive conversions
    """)

with challenges_col2:
    # Create impact assessment chart
    impact_data = pd.DataFrame({
        'Challenge': ['Fragmented Tags', 'Limited Cross-Domain', 'Manual Campaign Setup', 'Data Silos', 'Complex Attribution'],
        'Business Impact': [8, 7, 6, 9, 8],
        'Implementation Complexity': [6, 7, 5, 8, 7]
    })
    
    fig = px.scatter(
        impact_data,
        x='Implementation Complexity',
        y='Business Impact',
        text='Challenge',
        size=[40, 40, 40, 40, 40],  # Consistent size for all points
        color='Business Impact',
        color_continuous_scale=px.colors.sequential.Blues,
        title="Challenge Impact Assessment"
    )
    
    fig.update_traces(
        textposition='top center',
        marker=dict(
            line=dict(width=2, color=VERATHON_BLUE)
        )
    )
    
    fig.update_layout(
        xaxis=dict(
            title="Implementation Complexity",
            range=[0, 10]
        ),
        yaxis=dict(
            title="Business Impact",
            range=[0, 10]
        ),
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Digital Factory 24's Tag Management Solution
st.header("Digital Factory 24's Tag Management Solution")

st.markdown("""
### Integrated Tag Architecture for Verathon

Digital Factory 24 provides a comprehensive Google Tag Manager solution that addresses all of Verathon's current 
challenges while preparing for future marketing needs, including the launch of new product lines.
""")

solution_cols = st.columns(3)

with solution_cols[0]:
    st.markdown("""
    #### Unified Data Layer
    
    - Standardized data structure across all properties
    - Consistent event naming conventions
    - Automated parameter population
    - Enhanced e-commerce tracking
    - User dimension enrichment
    """)

with solution_cols[1]:
    st.markdown("""
    #### Intelligent Tag Orchestration
    
    - Centralized tag deployment and management
    - Conditional firing rules based on user behavior
    - Performance-optimized tag loading
    - Debug and preview environment
    - Version control and rollback capability
    """)

with solution_cols[2]:
    st.markdown("""
    #### Advanced Analytics Integration
    
    - Cross-domain user journey tracking
    - Multi-touch attribution modeling
    - Custom dimension and metric creation
    - Real-time data validation
    - Integration with CRM and marketing platforms
    """)

# GTM Implementation Process
st.header("Tag Management Implementation Process")

# Create a timeline chart for the implementation process
timeline_data = pd.DataFrame({
    'Phase': ['Discovery & Audit', 'Strategy & Architecture', 'Development & Testing', 'Deployment', 'Validation', 'Optimization'],
    'Duration': [2, 3, 4, 1, 2, 'Ongoing'],
    'Description': [
        'Comprehensive audit of existing tags and data needs',
        'Design data layer and tag architecture',
        'Build and test tag configurations',
        'Deploy to production environment',
        'Validate data accuracy and completeness',
        'Continuous refinement based on business needs'
    ],
    'Week': [1, 3, 6, 10, 11, 13]
})

# Create horizontal timeline
fig = go.Figure()

# Add timeline events
for i, row in timeline_data.iterrows():
    fig.add_trace(go.Scatter(
        x=[row['Week']],
        y=[0],
        mode='markers+text',
        marker=dict(
            size=30,
            color=VERATHON_BLUE,
            symbol='circle',
            line=dict(
                color='white',
                width=2
            )
        ),
        text=str(i+1),
        textfont=dict(
            color='white',
            size=14
        ),
        textposition='middle center',
        name=row['Phase'],
        hoverinfo='text',
        hovertext=f"{row['Phase']}: {row['Description']}"
    ))

# Add connecting line
fig.add_trace(go.Scatter(
    x=timeline_data['Week'],
    y=[0, 0, 0, 0, 0, 0],
    mode='lines',
    line=dict(color=VERATHON_BLUE, width=4),
    hoverinfo='skip',
    showlegend=False
))

# Update layout
fig.update_layout(
    title="Tag Manager Implementation Timeline (in weeks)",
    showlegend=True,
    height=200,
    margin=dict(l=0, r=0, t=50, b=0),
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=True,
        title="Week"
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False
    ),
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig, use_container_width=True)

# Add descriptions below the timeline
timeline_cols = st.columns(6)

for i, col in enumerate(timeline_cols):
    with col:
        st.markdown(f"**{i+1}. {timeline_data.iloc[i]['Phase']}**")
        st.markdown(f"{timeline_data.iloc[i]['Description']}")
        if i < 5:
            st.markdown(f"*Duration: {timeline_data.iloc[i]['Duration']} weeks*")
        else:
            st.markdown(f"*Duration: {timeline_data.iloc[i]['Duration']}*")

# New Product Launch GTM Tag Strategy
st.header("New Product Line Tag Management Strategy")

st.markdown("""
Digital Factory 24 has developed a specialized tag management strategy for Verathon's upcoming product line launch, 
ensuring comprehensive tracking from initial awareness through the complete customer journey.
""")

# Create a journey visualization
journey_stages = ['Awareness', 'Interest', 'Consideration', 'Intent', 'Evaluation', 'Purchase']
journey_metrics = ['Impressions', 'Engagement', 'Content Consumption', 'Product Detail Views', 'Comparison Actions', 'Conversion']
journey_tags = [
    'Impression tracking, View-through pixels', 
    'Interaction events, Video tracking', 
    'Content page tags, Scroll depth', 
    'Product view tags, Feature interaction', 
    'Comparison tools, Configurator events', 
    'Purchase funnel, Cart events'
]

journey_data = pd.DataFrame({
    'Stage': journey_stages,
    'Metrics': journey_metrics,
    'Tags': journey_tags,
    'Position': list(range(len(journey_stages))),
    'Size': [1] * len(journey_stages)
})

# Create journey flow visualization
fig = go.Figure()

# Add stages as nodes
for i, row in journey_data.iterrows():
    fig.add_trace(go.Scatter(
        x=[row['Position']],
        y=[0],
        mode='markers+text',
        marker=dict(
            symbol='circle',
            size=40,
            color=VERATHON_BLUE,
            line=dict(width=2, color='white')
        ),
        text=row['Stage'],
        textposition='bottom center',
        hoverinfo='text',
        hovertext=f"<b>{row['Stage']}</b><br>Key Metrics: {row['Metrics']}<br>Tag Types: {row['Tags']}",
        name=row['Stage']
    ))

# Add connecting arrows
for i in range(len(journey_data) - 1):
    fig.add_shape(
        type="line",
        x0=journey_data.iloc[i]['Position'] + 0.1,
        y0=0,
        x1=journey_data.iloc[i+1]['Position'] - 0.1,
        y1=0,
        line=dict(
            color=VERATHON_BLUE,
            width=3,
            dash="solid",
        ),
        xref="x",
        yref="y"
    )
    # Add arrow
    fig.add_annotation(
        x=(journey_data.iloc[i]['Position'] + journey_data.iloc[i+1]['Position']) / 2,
        y=0,
        ax=(journey_data.iloc[i]['Position'] + journey_data.iloc[i+1]['Position']) / 2 - 0.1,
        ay=0,
        xref="x",
        yref="y",
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor=VERATHON_BLUE
    )

# Update layout
fig.update_layout(
    title="Customer Journey Tag Implementation for New Product Line",
    showlegend=False,
    height=200,
    margin=dict(l=0, r=0, t=50, b=100),
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        range=[-0.5, len(journey_data) - 0.5]
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        range=[-0.5, 0.5]
    ),
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig, use_container_width=True)

# Add metrics and tags tables
metrics_col1, metrics_col2 = st.columns(2)

with metrics_col1:
    st.subheader("Key Metrics by Stage")
    metrics_df = pd.DataFrame({
        'Stage': journey_stages,
        'Primary Metrics': journey_metrics,
        'Supporting Metrics': [
            'Reach, Ad Viewability, CPM',
            'CTR, Time on Site, Bounce Rate',
            'Content Downloads, Form Starts',
            'Product Page Time, Spec Views',
            'Comparison Tool Usage, Reviews Read',
            'AOV, Conversion Rate, Revenue'
        ]
    })
    st.dataframe(metrics_df, use_container_width=True, hide_index=True)

with metrics_col2:
    st.subheader("Tag Implementation by Stage")
    tags_df = pd.DataFrame({
        'Stage': journey_stages,
        'Tag Types': journey_tags,
        'Integration Points': [
            'Ad Platforms, Social Media',
            'Website, Social Channels',
            'Content Hub, Resource Library',
            'Product Pages, Feature Demos',
            'Comparison Tools, Reviews',
            'Shopping Cart, Thank You Page'
        ]
    })
    st.dataframe(tags_df, use_container_width=True, hide_index=True)

# Attribution Modeling
st.header("Advanced Attribution Modeling")

st.markdown("""
One of Verathon's key challenges is understanding which marketing touchpoints truly drive conversions. 
Digital Factory 24 implements sophisticated attribution modeling to provide a clear view of marketing effectiveness.
""")

attribution_col1, attribution_col2 = st.columns([1, 1])

with attribution_col1:
    st.subheader("Multi-Touch Attribution")
    st.markdown("""
    Our attribution solution moves beyond simple last-click models to provide a holistic view of the customer journey:
    
    - **Data-Driven Attribution** - Machine learning algorithms that dynamically assign credit based on impact
    
    - **Custom Attribution Windows** - Configurable lookback windows for different channels and campaigns
    
    - **Cross-Device Tracking** - Connect user journeys across multiple devices and sessions
    
    - **Online-to-Offline Integration** - Link digital touchpoints to offline conversions
    
    - **Campaign Influence Reporting** - Understand which campaigns influence decisions even without direct conversions
    """)
    
    st.info("""
    **Implementation Note:** Digital Factory 24 will configure Google Analytics 4 with custom attribution models 
    and integrate with your CRM system to provide a complete view of the customer journey.
    """)

with attribution_col2:
    # Create a comparison of attribution models
    attribution_data = pd.DataFrame({
        'Channel': ['Paid Search', 'Email', 'Social', 'Organic Search', 'Direct', 'Referral'],
        'Last Click': [35, 15, 10, 20, 15, 5],
        'First Click': [25, 5, 30, 25, 10, 5],
        'Linear': [20, 20, 15, 20, 15, 10],
        'Data Driven': [22, 18, 18, 22, 12, 8]
    })
    
    fig = px.bar(
        attribution_data,
        x='Channel',
        y=['Last Click', 'First Click', 'Linear', 'Data Driven'],
        title="Attribution Model Comparison (% Credit)",
        barmode='group',
        color_discrete_sequence=[VERATHON_BLUE, '#6FA8DC', '#A2C4C9', '#9FC5E8']
    )
    
    fig.update_layout(height=400, yaxis_title="Conversion Credit (%)")
    st.plotly_chart(fig, use_container_width=True)

# Expert GTM Team
st.header("Digital Factory 24's Expert GTM Team")

team_col1, team_col2, team_col3 = st.columns(3)

with team_col1:
    st.subheader("Technical Expertise")
    st.markdown("""
    Our GTM specialists bring:
    
    - Google Tag Manager certification and advanced implementation experience
    - JavaScript & DOM expertise for custom tracking solutions
    - Experience with complex e-commerce tracking
    - Regular training on latest GTM capabilities
    - Custom variable and trigger development
    """)

with team_col2:
    st.subheader("Analytics Knowledge")
    st.markdown("""
    Our analytics experts deliver:
    
    - Advanced GA4 custom event configuration
    - Cross-domain tracking setup
    - Attribution model development
    - Custom dimension & metric creation
    - Automated reporting dashboards
    - Anomaly detection & alerts
    """)

with team_col3:
    st.subheader("24/7 Support Model")
    st.markdown("""
    Our support framework ensures:
    
    - Round-the-clock monitoring of tag performance
    - Immediate response to tracking issues
    - Regular tag audits and optimization
    - Proactive updates for browser changes
    - Campaign launch support
    - Ongoing training for your team
    """)

# Business impact section
st.header("Expected Business Impact")

# Create ROI projection chart
months = list(range(1, 13))
baseline_roi = [1.0] * 12
enhanced_roi = [1.0, 1.1, 1.3, 1.5, 1.7, 1.9, 2.1, 2.3, 2.4, 2.5, 2.6, 2.7]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=months,
    y=baseline_roi,
    mode='lines',
    name='Current Approach',
    line=dict(color='lightgray', width=3)
))

fig.add_trace(go.Scatter(
    x=months,
    y=enhanced_roi,
    mode='lines',
    name='With DF24 Tag Management Solution',
    line=dict(color=VERATHON_BLUE, width=3)
))

# Add shaded area between curves
fig.add_trace(go.Scatter(
    x=months+months[::-1],
    y=enhanced_roi+baseline_roi[::-1],
    fill='toself',
    fillcolor='rgba(0,86,167,0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    hoverinfo="skip",
    showlegend=False
))

# Annotate the ROI increase
fig.add_annotation(
    x=11,
    y=2.65,
    text="170% ROI Increase",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor=VERATHON_BLUE,
    font=dict(size=14, color=VERATHON_BLUE),
    ax=30,
    ay=-30
)

fig.update_layout(
    title="Projected Marketing ROI Over 12 Months",
    xaxis_title="Month",
    yaxis_title="Marketing ROI Multiple",
    yaxis=dict(range=[0, 3]),
    height=400,
    margin=dict(l=0, r=0, t=50, b=0)
)

st.plotly_chart(fig, use_container_width=True)

impact_col1, impact_col2 = st.columns(2)

with impact_col1:
    st.subheader("Quantitative Benefits")
    
    benefits_data = pd.DataFrame({
        'Metric': [
            'Campaign Setup Time', 
            'Data Collection Accuracy', 
            'Attribution Visibility', 
            'Marketing ROI', 
            'Time to Insight'
        ],
        'Improvement': [
            '-75%', 
            '+95%', 
            '+85%', 
            '+170%', 
            '-65%'
        ]
    })
    
    st.table(benefits_data)

with impact_col2:
    st.subheader("Qualitative Benefits")
    st.markdown("""
    Beyond the measurable improvements, our Tag Management solution delivers:
    
    - **Strategic Agility** - Faster implementation of new marketing initiatives
    
    - **Unified Customer View** - Complete understanding of the customer journey
    
    - **Data Confidence** - Trust in the accuracy and completeness of marketing data
    
    - **Marketing-Sales Alignment** - Shared understanding of channel effectiveness
    
    - **Optimization Culture** - Data-driven approach to continuous improvement
    """)

# Tag Management Call to action
st.markdown("---")
st.markdown(f"""
<div style="background-color:{VERATHON_BLUE}; padding:15px; border-radius:5px; text-align:center;">
    <h2 style="color:white;">Ready to transform your digital marketing measurement?</h2>
    <p style="color:white;">Contact your Digital Factory 24 representative to schedule a detailed Tag Management assessment and implementation plan.</p>
</div>
""", unsafe_allow_html=True)
