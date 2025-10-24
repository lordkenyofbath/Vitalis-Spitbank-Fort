import streamlit as st

st.set_page_config(page_title="Vitalis Spitbank - Investment Teaser", layout="wide")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=Montserrat:wght@300;400;600&display=swap');
    
    .main {
        background: white;
    }
    
    h1, h2, h3 {
        font-family: 'Cormorant Garamond', serif;
        font-weight: 300;
    }
    
    .header-box {
        text-align: center;
        border-bottom: 3px solid #92400e;
        padding-bottom: 20px;
        margin-bottom: 30px;
    }
    
    .header-title {
        font-size: 48px;
        color: #92400e;
        margin-bottom: 8px;
        letter-spacing: 2px;
        font-family: 'Cormorant Garamond', serif;
        font-weight: 300;
    }
    
    .tagline {
        font-size: 16px;
        color: #64748b;
        font-weight: 300;
        letter-spacing: 1px;
    }
    
    .exec-summary {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        padding: 20px;
        border-left: 4px solid #92400e;
        margin-bottom: 25px;
        font-size: 14px;
        line-height: 1.7;
        border-radius: 4px;
    }
    
    .stat-box {
        background: white;
        border: 1px solid #e2e8f0;
        padding: 20px;
        text-align: center;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    
    .stat-number {
        font-size: 32px;
        font-weight: 600;
        color: #92400e;
        margin-bottom: 8px;
    }
    
    .stat-label {
        font-size: 12px;
        color: #64748b;
    }
    
    .section-header {
        font-size: 24px;
        color: #92400e;
        margin-bottom: 12px;
        border-bottom: 2px solid #fbbf24;
        padding-bottom: 4px;
        font-family: 'Cormorant Garamond', serif;
        font-weight: 300;
    }
    
    .financial-box {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        color: white;
        padding: 30px;
        border-radius: 8px;
        margin: 20px 0;
    }
    
    .financial-value {
        font-size: 36px;
        font-weight: 600;
        color: #fbbf24;
        margin-bottom: 8px;
    }
    
    .cta-box {
        background: #92400e;
        color: white;
        padding: 30px;
        text-align: center;
        border-radius: 8px;
        margin: 20px 0;
    }
    
    .cta-title {
        color: #fbbf24;
        font-size: 28px;
        margin-bottom: 15px;
        font-family: 'Cormorant Garamond', serif;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class='header-box'>
    <h1 class='header-title'>VITALIS SPITBANK</h1>
    <p class='tagline'>UK's First Ultra-Luxury Wellness Fortress | Strategic Spa Partnership</p>
</div>
""", unsafe_allow_html=True)

# Executive Summary
st.markdown("""
<div class='exec-summary'>
<strong>CONFIDENTIAL INVESTMENT OPPORTUNITY:</strong> Acquire and reposition Spitbank Fort as "Vitalis Spitbank" – an ultra-exclusive, 9-suite wellness and longevity destination. This Grade II Listed Napoleonic fortress sits alone in the Solent, three miles off Portsmouth. With a world-leading Swiss luxury spa brand as partner and £9.2M total investment, the project targets UHNW clientele seeking transformative, science-backed wellness in complete seclusion. Stabilized Year 5 revenue of £4.6M with 15% yield on cost and 296% total 10-year ROI.
</div>
""", unsafe_allow_html=True)

# Two Column Layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h2 class='section-header'>The Asset</h2>", unsafe_allow_html=True)
    
    stats_col1, stats_col2 = st.columns(2)
    with stats_col1:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>9</div>
            <div class='stat-label'>Ultra-Luxury Suites</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>£1,500</div>
            <div class='stat-label'>Target ADR</div>
        </div>
        """, unsafe_allow_html=True)
    
    with stats_col2:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>33k</div>
            <div class='stat-label'>Square Feet</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>75%</div>
            <div class='stat-label'>Stabilized Occupancy</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("**Key Features:**")
    st.markdown("""
    - 150-year-old Grade II Listed fortress in the Solent
    - Accessible only by private boat or helicopter
    - 33,000 sq ft over 3 floors with roof terrace, hot pool, sauna
    - Existing infrastructure: generators, artesian well water
    - 15ft granite walls – completely private and secure
    """)
    
    st.markdown("<h2 class='section-header'>Strategic Partnership</h2>", unsafe_allow_html=True)
    st.markdown("**World-Leading Luxury Spa Partner**")
    st.markdown("""
    - Partnership with premier Swiss luxury spa and longevity brand
    - Swiss precision luxury aligns with UHNW positioning
    - UK flagship wellness destination for the brand
    - Revenue share model (20-30% of spa revenues)
    - Access to global UHNW network and brand validation
    - Institutional credibility for capital raising
    """)
    
    st.markdown("<h2 class='section-header'>Market Opportunity</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Target:** HNWIs/UHNWIs aged 40-60, proactive about longevity
    - **Gap:** UK lacks true ultra-luxury wellness destination
    - **Proximity:** 90 mins from London, 30 mins from Southampton Airport
    - **Use Cases:** Individual retreats, corporate leadership, private buyouts
    - **Seasonality:** Isle of Wight festivals, Cowes Week, Goodwood events
    """)

with col2:
    st.markdown("<h2 class='section-header'>Wellness Offering</h2>", unsafe_allow_html=True)
    st.markdown("**Science-Backed Longevity**")
    st.markdown("""
    - **Diagnostics:** Genetic testing, biomarkers, cognitive analysis
    - **Bio-Hacking:** Cryotherapy, HBOT, PEMF, red light therapy
    - **Holistic:** Ayurveda, acupuncture, sound baths, breathwork
    - **Fitness:** Personal training, rooftop yoga, sea-based activities
    - **Luxury Spa:** Advanced anti-aging facials, massage, IV therapy
    - **Culinary:** Sea-to-table, personalized nutrition, functional cuisine
    """)
    
    st.markdown("**Signature Packages**")
    st.markdown("""
    - **Vitalis Renewal** (3 days): Introduction to wellness principles
    - **Maritime Detox** (5 days): Comprehensive body/mind cleanse
    - **Longevity Voyage** (7+ days): Full transformation with take-home plan
    """)
    
    st.markdown("<h2 class='section-header'>Investment Highlights</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Unique Asset:** No comparable property globally – moat defensibility
    - **Strategic Partnership:** World-class spa brand de-risks operations
    - **Capital Light Post-Launch:** Low maintenance capex after refurbishment
    - **High Operating Leverage:** Small suite count = efficient staffing (18-22 FTEs)
    - **Multiple Exit Paths:** Trade sale, refinance, UHNW private acquisition
    - **Institutional Ready:** Trophy asset for sovereign funds, family offices
    """)
    
    st.markdown("<h2 class='section-header'>Development Timeline</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Months 1-6:** Design, planning, permits
    - **Months 7-18:** Construction, infrastructure upgrades
    - **Months 19-22:** Interior fit-out, FF&E installation
    - **Months 23-24:** Pre-opening, staff training, PR launch
    - **Target Opening:** Q4 2027
    """)

# Financial Snapshot
st.markdown("<h2 class='section-header'>Financial Snapshot</h2>", unsafe_allow_html=True)

fin_col1, fin_col2, fin_col3, fin_col4 = st.columns(4)

with fin_col1:
    st.markdown("""
    <div class='stat-box'>
        <div class='financial-value'>£9.2M</div>
        <div class='stat-label'>Total Investment</div>
    </div>
    """, unsafe_allow_html=True)

with fin_col2:
    st.markdown("""
    <div class='stat-box'>
        <div class='financial-value'>£4.6M</div>
        <div class='stat-label'>Year 5 Revenue</div>
    </div>
    """, unsafe_allow_html=True)

with fin_col3:
    st.markdown("""
    <div class='stat-box'>
        <div class='financial-value'>15.0%</div>
        <div class='stat-label'>Year 5 Yield on Cost</div>
    </div>
    """, unsafe_allow_html=True)

with fin_col4:
    st.markdown("""
    <div class='stat-box'>
        <div class='financial-value'>296%</div>
        <div class='stat-label'>10-Year Total ROI</div>
    </div>
    """, unsafe_allow_html=True)

# CTA
st.markdown("""
<div class='cta-box'>
    <h2 class='cta-title'>Partner with Us</h2>
    <p><strong>Seeking:</strong> Experienced wellness/luxury hotel operator + institutional equity partner</p>
    <p><strong>Structure:</strong> Operating partner (management contract or JV) + Capital partner (equity investment)</p>
    <p><strong>Next Steps:</strong> Detailed financial model | Site visit (helicopter transfer) | Strategic partner introduction</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #94a3b8; font-size: 12px;'>
Confidential & Proprietary | October 2025 | For Discussion Purposes Only<br>
Contact: [YOUR NAME] | [YOUR EMAIL] | [YOUR PHONE]
</div>
""", unsafe_allow_html=True)

# Download button
st.markdown("---")
st.info("💡 **To save as PDF:** Press Ctrl+P (Windows) or Cmd+P (Mac), then select 'Save as PDF'")
