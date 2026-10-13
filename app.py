import streamlit as st
from database.models import init_db
from database.seed_data import seed_database
from modules import dashboard, past_papers, mcq_database

# Initialize Database & Seed Data
init_db()
seed_database() # Yeh line app khulte hi demo data daal degi

# Page Configuration
st.set_page_config(
    page_title="Pakistan Exam Intelligence",
    page_icon="🇵🇰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; color: #007BFF; font-weight: bold; margin-bottom: 0px;}
    .sub-header { font-size: 1.2rem; color: #555; margin-bottom: 20px;}
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🎓 Navigation")
menu_options = [
    "🏠 Dashboard",
    "📄 Past Papers Library",
    "🧠 MCQs Master Database",
    "🤖 AI Paper Generator",
    "📰 Real-Time News Monitor",
    "📊 Performance Analytics"
]
choice = st.sidebar.radio("Go to:", menu_options)

# Routing Logic
if choice == "🏠 Dashboard":
    dashboard.render_dashboard()
elif choice == "📄 Past Papers Library":
    past_papers.render_past_papers()
elif choice == "🧠 MCQs Master Database":
    mcq_database.render_mcq_database()
elif choice == "🤖 AI Paper Generator":
    st.warning("Module 6 (AI Paper Generator) requires a Gemini API Key. Coming in Batch 3.")
elif choice == "📰 Real-Time News Monitor":
    st.warning("Module 5 (News Monitor) is coming in Batch 4.")
elif choice == "📊 Performance Analytics":
    st.info("Module 10 (Analytics) will be delivered in Batch 5.")
