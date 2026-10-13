# --- YE 3 LINES ERROR KO THEEK KARENGI ---
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# -----------------------------------------

import streamlit as st
from database.models import init_db
from database.seed_data import seed_database
from modules import dashboard, past_papers, mcq_database

# Database Initialize aur Data Seed Karein
init_db()
seed_database()

# Page Configuration
st.set_page_config(
    page_title="Pakistan Exam Intelligence",
    page_icon="🇵🇰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS (Professional Look)
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; color: #007BFF; font-weight: bold; margin-bottom: 0px;}
    .sub-header { font-size: 1.2rem; color: #555; margin-bottom: 20px;}
    .stButton>button { width: 100%; border-radius: 5px; background-color: #007BFF; color: white;}
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🎓 Navigation")
st.sidebar.markdown("---")

menu_options = [
    "🏠 Dashboard",
    "📄 Past Papers Library",
    "🧠 MCQs Master Database",
    "🤖 AI Paper Generator",
    "📰 Real-Time News Monitor",
    "📊 Performance Analytics",
    "⚙️ Admin Panel"
]

choice = st.sidebar.radio("Go to:", menu_options)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** Use the AI Paper Generator to create custom tests.")

# Routing Logic (Kaunsa Module Kahan Chalega)
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

elif choice == "⚙️ Admin Panel":
    st.info("Admin Panel will be available in future updates.")
