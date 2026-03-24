import streamlit as st
import plotly.express as px
import pandas as pd

# 1. Page Configuration for a professional look
st.set_page_config(page_title="NABH Strategic Analysis", layout="wide")

# 2. Data Preparation from the Report
data = {
    "Program": [
        "POI Hospital (6th Ed)", 
        "Quality Managers Course", 
        "Nursing Excellence", 
        "Front Office Induction", 
        "Clinical Trial Awareness"
    ],
    "Daily Revenue": [200000, 140000, 180000, 40000, 120000],
    "Daily Net Margin": [192000, 132000, 172000, 32000, 112000],
    "Margin %": [96, 94, 95, 80, 93],
    "Batch Size": [55, 45, 50, 100, 35]
}
df = pd.DataFrame(data)

# 3. Header and Executive Summary
st.title("🏥 NABH Training: Integrated Comparative & Rational Analysis")
st.markdown("---")

# 4. Key Metrics (KPIs)
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric("Top Daily Revenue", "₹2,00,000", delta="POI Hospital (6th Ed)")
with col_m2:
    st.metric("Highest Net Margin", "96%", delta="Operational Efficiency")
with col_m3:
    st.metric("Break-Even Point", "2 Participants", delta="Fixed Labor Protection")

# 5. Interactive Visuals Section
st.markdown("### Financial Performance & Strategic Logic")
col1, col2 = st.columns([1.5, 1])

with col1:
    st.subheader("Revenue Distribution")
    fig_pie = px.pie(
        df, values='Daily Revenue', names='Program', 
        hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel
    )
    # Using width='stretch' to ensure compatibility with latest Streamlit
    st.plotly_chart(fig_pie, width='stretch')

with col2:
    st.subheader("Rational Analysis (The 'Why')")
    selection = st.selectbox("Select a program to see the pricing logic:", df["Program"])
    
    # Custom Logic Explanations based on the Report
    if "POI" in selection or "Nursing" in selection:
        st.info("**Value-Based Pricing:** These generate the highest surplus. They transform participants into 'Internal Counsellors,' allowing hospitals to eliminate expensive external consultancy costs.")
    elif "Front Office" in selection:
        st.success("**Social Impact Logic:** Priced at ₹500 to prioritize 'Safety Culture.' By trading margin for volume (100 staff), we achieve the highest brand footprint.")
    else:
        st.write("**Technical Depth:** Fees for specialized courses account for high-level faculty expertise and rigorous technical standards.")

# 6. Sustainability Section
st.markdown("---")
st.header("Operational Sustainability")
st.write("Current programs operate at **80% to 96% net daily margins**, providing a buffer for growth.")

# Faculty cost table for quick reference
faculty_data = {
    "Duration": ["Full Day (> 4 Hours)", "Half Day (< 4 Hours)"],
    "Remuneration": ["₹8,000", "₹4,000"]
}
st.table(pd.DataFrame(faculty_data))

# 7. Data Download Feature
st.markdown("---")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Full Analysis Report (CSV)",
    data=csv,
    file_name='NABH_Analysis_Report.csv',
    mime='text/csv',
)
st.download_button(
    label="Download data as CSV",
    data=df.to_csv(index=False),
    file_name="data.csv",
    mime="text/csv"
)