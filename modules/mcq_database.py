import streamlit as st
import pandas as pd
from database.db_manager import get_db, add_mcq
from database.models import MCQ, Subject

def render_mcq_database():
    st.markdown('<div class="main-header">🧠 MCQs Master Database</div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🔍 Search & Practice", "➕ Add New MCQ"])
    
    db = next(get_db())
    
    with tab1:
        st.subheader("Search MCQs")
        col1, col2 = st.columns(2)
        with col1:
            subjects = [s.name for s in db.query(Subject).all()]
            selected_subject = st.selectbox("Select Subject", ["All"] + subjects)
        with col2:
            difficulty = st.selectbox("Difficulty", ["All", "Easy", "Medium", "Hard"])
            
        # Query DB
        query = db.query(MCQ)
        if selected_subject != "All":
            sub = db.query(Subject).filter(Subject.name == selected_subject).first()
            if sub: query = query.filter(MCQ.subject_id == sub.id)
        if difficulty != "All":
            query = query.filter(MCQ.difficulty == difficulty)
            
        mcqs = query.limit(50).all()
        
        if not mcqs:
            st.warning("No MCQs found. Please add new MCQs or run the Seed Data script.")
        else:
            st.success(f"Showing {len(mcqs)} MCQs")
            for i, mcq in enumerate(mcqs):
                with st.expander(f"Q{i+1}. {mcq.question[:100]}..."):
                    st.write(f"**A.** {mcq.option_a}")
                    st.write(f"**B.** {mcq.option_b}")
                    st.write(f"**C.** {mcq.option_c}")
                    st.write(f"**D.** {mcq.option_d}")
                    st.success(f"**Correct Answer:** {mcq.correct_answer}")
                    st.info(f"**Explanation:** {mcq.explanation}")
                    st.caption(f"Source: {mcq.source} | Status: {mcq.verification_status} | Difficulty: {mcq.difficulty}")

    with tab2:
        st.subheader("Add New MCQ")
        with st.form("add_mcq_form"):
            question = st.text_area("Question")
            col1, col2 = st.columns(2)
            with col1:
                opt_a = st.text_input("Option A")
                opt_b = st.text_input("Option B")
            with col2:
                opt_c = st.text_input("Option C")
                opt_d = st.text_input("Option D")
            
            correct = st.selectbox("Correct Answer", ["A", "B", "C", "D"])
            explanation = st.text_area("Detailed Explanation")
            subject = st.text_input("Subject (e.g., Physics)")
            difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
            source = st.text_input("Source Reference")
            
            submit = st.form_submit_button("Add MCQ")
            if submit:
                add_mcq(db, question, opt_a, opt_b, opt_c, opt_d, correct, explanation, subject, "", difficulty, source)
                st.success("MCQ added successfully!")
