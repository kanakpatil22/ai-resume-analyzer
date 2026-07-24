from src.extractor import extract_text
from src.analyzer import find_skills, calculate_score, check_resume_elements
from src.utils import save_report

resume_path = input("Enter the path of your resume (PDF or DOCX): ").strip()

try:
    resume_text = extract_text(resume_path)
    matched, missing = find_skills(resume_text)
    score = calculate_score(matched, missing)
    present_elements, missing_elements = check_resume_elements(resume_text)

    print("\n✅ Skills Found in Resume:")
    print(matched)

    print("\n❌ Skills Missing:")
    print(missing)

    print(f"\n📊 Resume Score: {score}%")

    print("\n📋 Resume Elements Present:")
    print(present_elements)

    print("\n⚠️ Resume Elements Missing (Consider Adding):")
    print(missing_elements)

    save_report(matched, missing, score)

except FileNotFoundError:
    print("\n⚠️ Error: File not found. Please check the path and try again.")

except ValueError as e:
    print(f"\n⚠️ Error: {e}")