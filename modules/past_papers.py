import streamlit as st
import pandas as pd
import os
from database.db_manager import get_db
from database.models import PastPaper

def render_past_papers():
    st.markdown('<div class="main-header">📄 Past Papers Library</div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🔍 Browse Past Papers", "📤 Upload & Extract"])
    
    db = next(get_db())
    
    with tab1:
        st.subheader("Browse Previous Years' Papers")
        col1, col2, col3 = st.columns(3)
        with col1:
            commission = st.selectbox("Commission", ["All", "PPSC", "FPSC", "CSS", "PMS"])
        with col2:
            year = st.selectbox("Year", ["All", "2024", "2023", "2022", "2021"])
        with col3:
            dept = st.text_input("Search Department/Post")
            
        # Fetch from DB
        query = db.query(PastPaper)
        if commission != "All":
            query = query.filter(PastPaper.commission == commission)
        if year != "All":
            query = query.filter(PastPaper.year == int(year))
        papers = query.all()
        
        if papers:
            df = pd.DataFrame([{
                "Commission": p.commission, "Year": p.year, "Department": p.department,
                "Post": p.post_name, "Type": p.paper_type, "Marks": p.total_marks
            } for p in papers])
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No papers found for this filter. Upload a PDF to add new papers.")

    with tab2:
        st.subheader("Upload Past Paper PDF")
        st.write("Upload a PDF file. The system will try to extract MCQs automatically.")
        uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
        if uploaded_file is not None:
            # Save file
            file_path = os.path.join("uploads", uploaded_file.name)
            os.makedirs("uploads", exist_ok=True)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.success(f"File saved to {file_path}")
            
            if st.button("Extract MCQs from PDF"):
                with st.spinner("Extracting text and processing..."):
                    # Placeholder for PDF extraction logic
                    st.info("PDF Extraction module (OCR/AI) will be fully implemented in Batch 4. For now, paper metadata is saved.")
                    
                    # Save metadata to DB (Demo)
                    new_paper = PastPaper(
                        commission="PPSC", year=2024, department="Demo Dept", 
                        post_name="Demo Post", paper_type="MCQs", 
                        total_marks=100, difficulty="Medium", file_path=file_path
                    )
                    db.add(new_paper)
                    db.commit()
                    st.success("Paper metadata added to database!")
