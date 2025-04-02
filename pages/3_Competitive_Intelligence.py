import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(page_title="Competitive Intelligence", page_icon="🔍", layout="wide")

# Dashboard title
st.title("Competitive Intelligence Dashboard")

# Filter section
col1, col2 = st.columns(2)

with col1:
    competitors = st.multiselect(
        "Select Competitors",
        ["Verathon", "Competitor A", "Competitor B", "Competitor C", "Competitor D"],
        default=["Verathon", "Competitor A", "Competitor B"]
    )

with col2:
    timeframe = st.selectbox(
        "Analysis Timeframe",
        ["Last 30 Days", "Last Quarter", "Last 6 Months", "Year to Date"]
    )

# Main dashboard content
if len(competitors) > 0:
    # Comparative market position
    st.subheader("Market Position Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Market share data
        market_share = pd.DataFrame({
            'Company': ["Verathon", "Competitor A", "Competitor B", "Competitor C", "Competitor D", "Others"],
            'Share': [28, 22, 18, 12, 8, 12]
        })
        
        fig = px.pie(
            market_share, 
            values='Share', 
            names='Company',
            title='Estimated Market Share (%)',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        
        # Highlight Verathon
        fig.update_traces(
            marker=dict(
                line=dict(color='#000000', width=2)
            ),
            selector=dict(name='Verathon')
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Product positioning matrix
        positioning_data = pd.DataFrame({
            'Company': competitors,
            'Price': [85, 70, 90, 65, 55],
            'Quality': [90, 75, 85, 60, 50],
            'Market Share': [28, 22, 18, 12, 8]
        })
        
        fig = px.scatter(
            positioning_data, 
            x='Price', 
            y='Quality', 
            size='Market Share',
            color='Company',
            title='Product Positioning Matrix',
            size_max=50,
            labels={
                'Price': 'Price Point (Relative)',
                'Quality': 'Quality Perception (Relative)'
            }
        )
        
        # Add quadrant lines and labels
        fig.add_shape(
            type="line", line=dict(dash="dash"),
            x0=50, y0=70, x1=95, y1=70
        )
        fig.add_shape(
            type="line", line=dict(dash="dash"),
            x0=70, y0=50, x1=70, y1=95
        )
        
        # Add quadrant annotations
        fig.add_annotation(x=60, y=80, text="Premium Value", showarrow=False)
        fig.add_annotation(x=80, y=80, text="Premium", showarrow=False)
        fig.add_annotation(x=60, y=60, text="Economy", showarrow=False)
        fig.add_annotation(x=80, y=60, text="Overpriced", showarrow=False)
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Digital presence comparison
    st.subheader("Digital Presence Comparison")
    
    # Digital metrics data
    digital_metrics = pd.DataFrame({
        'Metric': [
            'Website Traffic (K/mo)', 
            'Domain Authority', 
            'Keyword Rankings', 
            'Social Following (K)', 
            'Media Mentions',
            'Review Score'
        ],
        'Verathon': [120, 65, 428, 35, 42, 4.5],
        'Competitor A': [95, 58, 352, 48, 38, 4.2],
        'Competitor B': [105, 62, 387, 22, 29, 4.3],
        'Competitor C': [65, 48, 245, 18, 22, 4.0],
        'Competitor D': [45, 42, 198, 12, 15, 3.8]
    })
    
    # Filter the DataFrame based on selected competitors
    digital_metrics_filtered = digital_metrics.copy()
    cols_to_keep = ['Metric'] + [c for c in competitors if c in digital_metrics.columns]
    digital_metrics_filtered = digital_metrics_filtered[cols_to_keep]
    
    # Function to highlight Verathon
    def highlight_verathon(df):
        if 'Verathon' in df.columns:
            return ['background-color: #e6f2ff' if col == 'Verathon' else '' for col in df.columns]
        return ['' for col in df.columns]
    
    # Function to highlight max value in each row
    def highlight_max(s):
        is_max = s == s.max()
        return ['background-color: #d4edda' if v else '' for v in is_max]
    
    # Apply styling
    styled_metrics = digital_metrics_filtered.style \
        .apply(highlight_max, axis=1, subset=[c for c in cols_to_keep if c != 'Metric']) \
        .apply(highlight_verathon, axis=1)
    
    st.dataframe(styled_metrics, use_container_width=True)
    
    # Digital footprint radar chart
    st.subheader("Digital Footprint Comparison")
    
    # Prepare data for radar chart
    categories = ['SEO Strength', 'Social Presence', 'Content Marketing', 'Online Advertising', 'PR/Media', 'Reviews']
    
    digital_footprint = {
        'Verathon': [85, 70, 90, 75, 80, 85],
        'Competitor A': [75, 85, 70, 80, 75, 80],
        'Competitor B': [80, 60, 85, 70, 65, 85],
        'Competitor C': [65, 70, 60, 50, 55, 75],
        'Competitor D': [55, 50, 45, 60, 40, 65]
    }
    
    # Filter based on selected competitors
    selected_footprints = {k: v for k, v in digital_footprint.items() if k in competitors}
    
    # Create radar chart
    fig = go.Figure()
    
    for company, values in selected_footprints.items():
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name=company
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=True,
        title="Digital Footprint Comparison"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabs for detailed competitive analysis
    tab1, tab2, tab3 = st.tabs(["Content Strategy", "SEO Performance", "Social Media"])
    
    with tab1:
        st.subheader("Content Strategy Comparison")
        
        # Content volume by type
        content_data = pd.DataFrame({
            'Content Type': ['Blog Posts', 'Whitepapers', 'Case Studies', 'Videos', 'Webinars', 'Infographics'],
            'Verathon': [45, 12, 8, 24, 18, 15],
            'Competitor A': [38, 8, 12, 36, 12, 10],
            'Competitor B': [42, 15, 6, 18, 24, 8],
            'Competitor C': [25, 6, 4, 12, 8, 6],
            'Competitor D': [18, 4, 2, 8, 6, 4]
        })
        
        # Filter based on selected competitors
        content_data_filtered = content_data.copy()
        cols_to_keep = ['Content Type'] + [c for c in competitors if c in content_data.columns]
        content_data_filtered = content_data_filtered[cols_to_keep]
        
        fig = px.bar(
            content_data_filtered, 
            x='Content Type', 
            y=[c for c in cols_to_keep if c != 'Content Type'],
            title='Content Volume by Type (Last 6 Months)',
            barmode='group'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Content focus areas
        st.subheader("Content Focus Areas")
        
        focus_data = {
            'Verathon': {
                'Areas': ['Product Features', 'Clinical Outcomes', 'ROI/Cost Savings', 'Implementation', 'Regulatory', 'Industry Trends'],
                'Percentages': [35, 25, 15, 10, 5, 10]
            },
            'Competitor A': {
                'Areas': ['Product Features', 'Clinical Outcomes', 'ROI/Cost Savings', 'Implementation', 'Regulatory', 'Industry Trends'],
                'Percentages': [40, 20, 10, 15, 5, 10]
            },
            'Competitor B': {
                'Areas': ['Product Features', 'Clinical Outcomes', 'ROI/Cost Savings', 'Implementation', 'Regulatory', 'Industry Trends'],
                'Percentages': [30, 30, 15, 5, 10, 10]
            }
        }
        
        col1, col2 = st.columns(2)
        
        for i, company in enumerate([c for c in competitors if c in focus_data]):
            data = focus_data[company]
            with col1 if i % 2 == 0 else col2:
                fig = px.pie(
                    names=data['Areas'],
                    values=data['Percentages'],
                    title=f"{company} - Content Focus Distribution"
                )
                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("SEO Performance Comparison")
        
        # SEO metrics
        seo_data = pd.DataFrame({
            'Metric': [
                'Organic Traffic (K/mo)', 
                'Keyword Rankings Top 3', 
                'Keyword Rankings Top 10',
                'Backlinks',
                'Referring Domains',
                'Domain Rating'
            ],
            'Verathon': [75, 42, 156, 3250, 428, 65],
            'Competitor A': [62, 38, 142, 2850, 382, 58],
            'Competitor B': [68, 45, 138, 3120, 405, 62],
            'Competitor C': [41, 24, 98, 1820, 245, 48],
            'Competitor D': [28, 18, 76, 1250, 198, 42]
        })
        
        # Filter based on selected competitors
        seo_data_filtered = seo_data.copy()
        cols_to_keep = ['Metric'] + [c for c in competitors if c in seo_data.columns]
        seo_data_filtered = seo_data_filtered[cols_to_keep]
        
        # Apply styling
        styled_seo = seo_data_filtered.style \
            .apply(highlight_max, axis=1, subset=[c for c in cols_to_keep if c != 'Metric']) \
            .apply(highlight_verathon, axis=1)
        
        st.dataframe(styled_seo, use_container_width=True)
        
        # Organic traffic trend
        st.subheader("Organic Traffic Trend")
        
        # Generate sample traffic trend data
        dates = pd.date_range(start='2023-01-01', periods=12, freq='M')
        
        traffic_trends = pd.DataFrame({
            'Date': dates,
            'Verathon': [55, 58, 62, 65, 68, 70, 72, 74, 76, 78, 75, 75],
            'Competitor A': [50, 52, 55, 57, 60, 62, 63, 65, 66, 64, 63, 62],
            'Competitor B': [60, 62, 64, 65, 66, 67, 68, 67, 68, 69, 68, 68],
            'Competitor C': [32, 34, 36, 38, 40, 42, 42, 43, 43, 42, 41, 41],
            'Competitor D': [22, 23, 24, 25, 26, 27, 27, 28, 28, 29, 28, 28]
        })
        
        # Filter based on selected competitors
        cols_to_plot = [c for c in competitors if c in traffic_trends.columns]
        
        fig = px.line(
            traffic_trends, 
            x='Date', 
            y=cols_to_plot,
            title='Organic Traffic Trend (K/month)',
            labels={'value': 'Traffic (K)', 'variable': 'Company'},
            line_shape='spline'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    with tab3:
        st.subheader("Social Media Performance")
        
        # Social media metrics
        social_data = pd.DataFrame({
            'Platform': ['LinkedIn', 'Twitter', 'Facebook', 'YouTube', 'Instagram'],
            'Verathon': [25000, 8500, 6200, 4500, 3200],
            'Competitor A': [32000, 12000, 8500, 6700, 5200],
            'Competitor B': [18000, 7500, 5600, 5200, 2800],
            'Competitor C': [12000, 5000, 4200, 3500, 2000],
            'Competitor D': [8000, 3500, 2800, 2200, 1500]
        })
        
        # Filter based on selected competitors
        social_data_filtered = social_data.copy()
        cols_to_keep = ['Platform'] + [c for c in competitors if c in social_data.columns]
        social_data_filtered = social_data_filtered[cols_to_keep]
        
        fig = px.bar(
            social_data_filtered,
            x='Platform',
            y=[c for c in cols_to_keep if c != 'Platform'],
            title='Social Media Following by Platform',
            barmode='group'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Engagement metrics
        st.subheader("Social Media Engagement")
        
        engagement_data = pd.DataFrame({
            'Metric': ['Avg. Post Engagement Rate', 'Avg. Comments per Post', 'Shares per Post', 'Link Clicks per Post'],
            'Verathon': [2.8, 18, 24, 35],
            'Competitor A': [3.2, 22, 28, 42],
            'Competitor B': [2.5, 16, 22, 28],
            'Competitor C': [1.8, 10, 15, 22],
            'Competitor D': [1.5, 8, 12, 18]
        })
        
        # Filter based on selected competitors
        engagement_data_filtered = engagement_data.copy()
        cols_to_keep = ['Metric'] + [c for c in competitors if c in engagement_data.columns]
        engagement_data_filtered = engagement_data_filtered[cols_to_keep]
        
        # Apply styling
        styled_engagement = engagement_data_filtered.style \
            .apply(highlight_max, axis=1, subset=[c for c in cols_to_keep if c != 'Metric']) \
            .apply(highlight_verathon, axis=1)
        
        st.dataframe(styled_engagement, use_container_width=True)
        
        # Content type performance
        st.subheader("Content Type Performance (LinkedIn)")
        
        content_perf = pd.DataFrame({
            'Content Type': ['Product Updates', 'Industry News', 'Case Studies', 'Educational', 'Company Culture'],
            'Verathon': [3.2, 2.5, 4.1, 3.8, 2.9],
            'Competitor A': [3.5, 2.8, 3.8, 4.2, 3.4],
            'Competitor B': [2.8, 2.3, 3.9, 3.5, 2.5],
            'Competitor C': [2.2, 1.9, 3.1, 2.8, 2.0],
            'Competitor D': [1.8, 1.5, 2.5, 2.3, 1.7]
        })
        
        # Filter based on selected competitors
        content_perf_filtered = content_perf.copy()
        cols_to_keep = ['Content Type'] + [c for c in competitors if c in content_perf.columns]
        content_perf_filtered = content_perf_filtered[cols_to_keep]
        
        fig = px.bar(
            content_perf_filtered,
            x='Content Type',
            y=[c for c in cols_to_keep if c != 'Content Type'],
            title='Engagement Rate by Content Type (%)',
            barmode='group'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Competitive product matrix
    st.markdown("---")
    st.subheader("Competitive Product Comparison Matrix")
    
    # Product feature comparison
    product_features = pd.DataFrame({
        'Feature Category': [
            'Core Functionality', 
            'Technology', 
            'Ease of Use', 
            'Integration Capabilities',
            'Support Services',
            'Pricing'
        ],
        'Verathon Position': ['Leader', 'Leader', 'Strong', 'Strong', 'Leader', 'Premium'],
        'Competitive Advantage': [
            'Superior accuracy and reliability',
            'Advanced AI-based imaging',
            'Intuitive interface with minimal training required',
            'Seamless EMR integration with all major providers',
            '24/7 clinical support with rapid response',
            'Premium pricing justified by outcomes and support'
        ],
        'Competitor Strengths': [
            'Competitor B offers similar accuracy',
            'Competitor A has comparable technology in specific use cases',
            'Competitor C markets simplified learning curve',
            'All major competitors offer standard integrations',
            'Competitors lack 24/7 clinical support',
            'Competitor D offers lower-cost alternative with fewer features'
        ],
        'Gap Analysis': [
            'Maintain accuracy advantage with ongoing validation studies',
            'Accelerate AI roadmap to maintain leadership position',
            'Address learning curve feedback in next UI update',
            'Develop unique integration capabilities with emerging platforms',
            'Highlight support advantage in marketing materials',
            'Consider tiered pricing model for price-sensitive segments'
        ]
    })
    
    st.dataframe(product_features, hide_index=True, use_container_width=True)
    
    # Customer perception heat map
    st.subheader("Customer Perception Heatmap")
    
    perception_data = pd.DataFrame({
        'Attribute': [
            'Product Quality', 
            'Reliability', 
            'Innovation', 
            'Customer Service',
            'Value for Money',
            'Brand Reputation'
        ],
        'Verathon': [90, 92, 85, 88, 75, 88],
        'Competitor A': [82, 85, 80, 76, 78, 80],
        'Competitor B': [85, 88, 78, 72, 82, 82],
        'Competitor C': [72, 75, 65, 68, 80, 70],
        'Competitor D': [65, 70, 60, 65, 88, 65]
    })
    
    # Filter based on selected competitors
    perception_data_filtered = perception_data.copy()
    cols_to_keep = ['Attribute'] + [c for c in competitors if c in perception_data.columns]
    perception_data_filtered = perception_data_filtered[cols_to_keep]
    
    # Create heatmap
    fig = px.imshow(
        perception_data_filtered.set_index('Attribute'),
        text_auto=True,
        labels=dict(x="Company", y="Attribute", color="Score"),
        x=[c for c in cols_to_keep if c != 'Attribute'],
        y=perception_data_filtered['Attribute'],
        color_continuous_scale='Bluyl',
        title="Customer Perception Scores (0-100)"
    )
    
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Please select at least one competitor to analyze.")
