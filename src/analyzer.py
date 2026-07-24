from src.config import SKILLS_LIST

def find_skills(resume_text):
    """
    Checks which skills from SKILLS_LIST are present in the resume text.
    Returns two lists: matched skills and missing skills.
    """
    resume_text_lower = resume_text.lower()
    
    matched_skills = []
    missing_skills = []
    
    for skill in SKILLS_LIST:
        if skill in resume_text_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)
    
    return matched_skills, missing_skills

def calculate_score(matched_skills, missing_skills):
    """
    Calculates resume score as a percentage based on matched vs total skills.
    """
    total_skills = len(matched_skills) + len(missing_skills)
    
    if total_skills == 0:
        return 0
    
    score = (len(matched_skills) / total_skills) * 100
    return round(score, 2)