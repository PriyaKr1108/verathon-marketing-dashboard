import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Go-To-Market Strategy - Verathon",
    page_icon="🚀",
    layout="wide"
)

# Verathon brand colors
VERATHON_BLUE = "#0056A7"
VERATHON_WHITE = "#FFFFFF"

# Header
st.markdown(f'<h1 style="color:{VERATHON_BLUE};">Go-To-Market Strategy</h1>', unsafe_allow_html=True)
st.markdown("Comprehensive Go-To-Market strategy for Verathon's new product launch")

# GTM Overview
st.header("Strategic GTM Framework")

# Create columns for the overview
gtm_overview_col1, gtm_overview_col2 = st.columns([1, 1])

with gtm_overview_col1:
    st.markdown("""
    ### Accelerated GTM Approach
    
    Digital Factory 24's proprietary Go-To-Market framework is designed specifically for medical device companies 
    launching new products. Our approach emphasizes:
    
    - **Speed-to-Market** - Accelerated launch timelines without sacrificing quality
    - **Strategic Positioning** - Clear differentiation based on competitive analysis
    - **Channel Optimization** - Prioritized channel mix based on ROI potential
    - **Targeted Messaging** - Persona-based communication strategies
    - **Measurement Framework** - Complete attribution and performance tracking
    """)
    
    st.button("Download Complete GTM Framework", key="gtm_download")

with gtm_overview_col2:
    # Create a radar chart for GTM capabilities
    gtm_dimensions = [
        'Market Intelligence',
        'Channel Strategy',
        'Content Development',
        'Campaign Execution',
        'Lead Management',
        'Performance Tracking'
    ]
    
    # Create GTM capability scores (current vs target)
    current_scores = [4, 3, 5, 4, 3, 2]
    target_scores = [9, 8, 9, 8, 9, 9]
    
    # Create the radar chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=current_scores,
        theta=gtm_dimensions,
        fill='toself',
        name='Current Capabilities',
        line_color='lightgray'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=target_scores,
        theta=gtm_dimensions,
        fill='toself',
        name='With DF24 GTM Strategy',
        line_color=VERATHON_BLUE
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )
        ),
        title="GTM Capability Enhancement",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Channel effectiveness
st.header("Channel Effectiveness Analysis")

# Create sample data for channel effectiveness
channel_data = pd.DataFrame({
    'Channel': ['Paid Search', 'Email Marketing', 'Medical Conferences', 'Content Marketing', 'Direct Sales', 'Partner Marketing'],
    'Reach': [8, 5, 7, 6, 4, 9],
    'Conversion': [7, 8, 6, 5, 9, 7],
    'Cost Efficiency': [6, 9, 5, 8, 3, 6],
    'Time to Impact': [8, 7, 5, 6, 8, 4]
})

# Calculate effectiveness score (weighted average)
channel_data['Effectiveness Score'] = (
    channel_data['Reach'] * 0.25 + 
    channel_data['Conversion'] * 0.35 + 
    channel_data['Cost Efficiency'] * 0.25 + 
    channel_data['Time to Impact'] * 0.15
).round(1)

# Sort by effectiveness score
channel_data = channel_data.sort_values('Effectiveness Score', ascending=False).reset_index(drop=True)

# Create visualization
channel_col1, channel_col2 = st.columns([3, 2])

with channel_col1:
    # Create horizontal bar chart of effectiveness scores
    fig = px.bar(
        channel_data,
        y='Channel',
        x='Effectiveness Score',
        orientation='h',
        color='Effectiveness Score',
        color_continuous_scale=px.colors.sequential.Blues,
        title="Channel Effectiveness Score (1-10)",
        labels={'Effectiveness Score': 'Overall Score (1-10)'}
    )
    
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with channel_col2:
    # Display the detailed metrics table
    st.markdown("### Channel Scoring Components")
    
    # Format the data for display
    display_df = channel_data[['Channel', 'Reach', 'Conversion', 'Cost Efficiency', 'Time to Impact', 'Effectiveness Score']]
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Scoring Weights:**
    - Reach: 25%
    - Conversion: 35%
    - Cost Efficiency: 25%
    - Time to Impact: 15%
    """)

# Launch Timeline
st.header("Product Launch Timeline")

# Create data for the launch timeline
launch_phases = [
    'Market Research & Analysis',
    'Messaging & Positioning',
    'Marketing Asset Development',
    'Sales Enablement',
    'Channel Activation',
    'Launch Execution',
    'Post-Launch Optimization'
]

# Days before/after launch
phase_start = [-90, -75, -60, -45, -30, 0, 15]
phase_end = [-76, -61, -46, -31, 1, 14, 90]

# Create a dataframe for the timeline
launch_df = pd.DataFrame({
    'Phase': launch_phases,
    'Start': phase_start,
    'End': phase_end,
    'Duration': [phase_end[i] - phase_start[i] for i in range(len(launch_phases))]
})

# Add categories for color coding
launch_df['Category'] = ['Planning', 'Planning', 'Development', 'Development', 'Execution', 'Execution', 'Optimization']

# Create Gantt chart
fig = px.timeline(
    launch_df,
    x_start='Start',
    x_end='End',
    y='Phase',
    color='Category',
    title="Launch Timeline (Days Relative to Launch Day)",
    color_discrete_map={
        'Planning': '#9FC5E8',
        'Development': '#6FA8DC',
        'Execution': VERATHON_BLUE,
        'Optimization': '#3C78D8'
    }
)

# Add a vertical line for launch day
fig.add_vline(x=0, line_width=2, line_dash="dash", line_color="green", annotation_text="Launch Day")

fig.update_layout(height=400)
fig.update_xaxes(title="Days Relative to Launch")

st.plotly_chart(fig, use_container_width=True)

# Launch Checklist
st.header("Launch Readiness Checklist")

checklist_col1, checklist_col2 = st.columns(2)

with checklist_col1:
    st.markdown("""
    ### Pre-Launch Checklist
    
    - [ ] Competitive analysis completed
    - [ ] Product positioning finalized
    - [ ] Target personas defined
    - [ ] Key messaging developed
    - [ ] Value proposition validated
    - [ ] GTM strategy document finalized
    - [ ] Marketing assets created
    - [ ] Website updates implemented
    - [ ] Tracking systems configured
    - [ ] Sales team trained
    """)
    
    st.button("Generate Complete Pre-Launch Checklist", key="prelaunch_btn")

with checklist_col2:
    st.markdown("""
    ### Launch & Post-Launch
    
    - [ ] Press releases distributed
    - [ ] Social campaigns activated
    - [ ] Email campaigns triggered
    - [ ] Partner communications sent
    - [ ] Sales enablement materials distributed
    - [ ] Dashboard monitoring established
    - [ ] Customer feedback collection activated
    - [ ] Initial performance review scheduled
    - [ ] Optimization plan in place
    - [ ] 30/60/90 day checkpoints scheduled
    """)
    
    st.button("Generate Complete Launch Checklist", key="launch_btn")

# Success Metrics
st.header("Success Metrics & Measurement")

metrics_col1, metrics_col2, metrics_col3 = st.columns(3)

with metrics_col1:
    st.markdown("### Awareness Metrics")
    st.markdown("""
    - Website traffic growth
    - Social media engagement
    - Press release pickups
    - Share of voice
    - Brand search volume
    - Competitor comparison rate
    """)

with metrics_col2:
    st.markdown("### Conversion Metrics")
    st.markdown("""
    - Lead generation rate
    - Marketing qualified leads
    - Sales qualified leads
    - Sales opportunity creation
    - Deal velocity
    - Funnel conversion rates
    """)

with metrics_col3:
    st.markdown("### Business Metrics")
    st.markdown("""
    - Revenue growth
    - Market share gain
    - Customer acquisition cost
    - Customer lifetime value
    - ROI by marketing channel
    - Revenue/Marketing spend ratio
    """)

# Revenue Forecast
st.header("Revenue Impact Forecast")

# Create sample revenue forecast data
months = list(range(1, 13))
traditional_launch = [0, 25000, 60000, 100000, 150000, 200000, 240000, 275000, 300000, 315000, 325000, 335000]
accelerated_launch = [0, 50000, 120000, 200000, 260000, 310000, 350000, 380000, 410000, 430000, 445000, 460000]

# Create forecast chart
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=months,
    y=traditional_launch,
    mode='lines+markers',
    name='Traditional Approach',
    line=dict(color='lightgray', width=3)
))

fig.add_trace(go.Scatter(
    x=months,
    y=accelerated_launch,
    mode='lines+markers',
    name='DF24 Accelerated Approach',
    line=dict(color=VERATHON_BLUE, width=3)
))

# Add shaded area between curves
fig.add_trace(go.Scatter(
    x=months+months[::-1],
    y=accelerated_launch+traditional_launch[::-1],
    fill='toself',
    fillcolor='rgba(0,86,167,0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    hoverinfo="skip",
    showlegend=False
))

# Annotate the revenue improvement
fig.add_annotation(
    x=10,
    y=425000,
    text="37% Higher Revenue",
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
    title="Projected Revenue Over 12 Months",
    xaxis_title="Month After Launch",
    yaxis_title="Revenue ($)",
    height=400
)

st.plotly_chart(fig, use_container_width=True)

# Go-To-Market CTA
st.markdown("---")
st.markdown(f"""
<div style="background-color:{VERATHON_BLUE}; padding:15px; border-radius:5px; text-align:center;">
    <h2 style="color:white;">Ready to accelerate your product launch?</h2>
    <p style="color:white;">Contact your Digital Factory 24 representative to schedule a GTM strategy session for your new product line.</p>
</div>
""", unsafe_allow_html=True)
