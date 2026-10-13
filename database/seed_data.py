from database.models import SessionLocal, Subject, MCQ, PastPaper, init_db

def seed_database():
    init_db()
    db = SessionLocal()
    
    # Check if already seeded
    if db.query(MCQ).count() > 0:
        print("Database already seeded.")
        return

    # 1. Add Subjects
    subjects = ["Physics", "Chemistry", "Biology", "English", "General Knowledge", "Pakistan Studies", "Islamic Studies", "Computer Science"]
    for sub_name in subjects:
        if not db.query(Subject).filter(Subject.name == sub_name).first():
            db.add(Subject(name=sub_name, category="General"))
    db.commit()

    # 2. Add Demo Past Papers
    papers = [
        PastPaper(commission="PPSC", year=2023, department="Miscellaneous", post_name="Assistant (BS-16)", paper_type="MCQs", total_marks=100, difficulty="Medium"),
        PastPaper(commission="FPSC", year=2024, department="Finance", post_name="Deputy Accountant", paper_type="MCQs", total_marks=100, difficulty="Hard"),
        PastPaper(commission="CSS", year=2023, department="Federal", post_name="CSS Compulsory", paper_type="Descriptive", total_marks=100, difficulty="Hard")
    ]
    db.add_all(papers)
    db.commit()

    # 3. Add Demo MCQs (Clearly labeled as demo)
    demo_mcqs = [
        MCQ(question="What is the capital of Pakistan?", option_a="Karachi", option_b="Lahore", option_c="Islamabad", option_d="Peshawar", correct_answer="C", explanation="Islamabad is the capital city of Pakistan.", subject_id=1, difficulty="Easy", source="Demo Data", verification_status="Verified"),
        MCQ(question="Who is the founder of Pakistan?", option_a="Allama Iqbal", option_b="Quaid-e-Azam", option_c="Liaquat Ali Khan", option_d="Sir Syed Ahmad Khan", correct_answer="B", explanation="Quaid-e-Azam Muhammad Ali Jinnah is the founder of Pakistan.", subject_id=6, difficulty="Easy", source="Demo Data", verification_status="Verified"),
        MCQ(question="Which is the largest continent by area?", option_a="Africa", option_b="Asia", option_c="Europe", option_d="North America", correct_answer="B", explanation="Asia is the largest continent, covering about 30% of Earth's land area.", subject_id=5, difficulty="Easy", source="Demo Data", verification_status="Verified"),
        MCQ(question="What is the chemical symbol for water?", option_a="H2O", option_b="CO2", option_c="O2", option_d="NaCl", correct_answer="A", explanation="Water is composed of two hydrogen atoms and one oxygen atom, hence H2O.", subject_id=2, difficulty="Easy", source="Demo Data", verification_status="Verified")
    ]
    db.add_all(demo_mcqs)
    db.commit()
    db.close()
    print("Database seeded successfully with demo data.")

if __name__ == "__main__":
    seed_database()
