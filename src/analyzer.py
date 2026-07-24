from src.config import SKILLS_LIST, RESUME_ELEMENTS

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

def check_resume_elements(resume_text):
    """
    Checks which important resume elements/sections are present or missing.
    """
    resume_text_lower = resume_text.lower()
    
    present_elements = []
    missing_elements = []
    
    for element in RESUME_ELEMENTS:
        if element in resume_text_lower:
            present_elements.append(element)
        else:
            missing_elements.append(element)
    
    return present_elements, missing_elements

def check_resume_length(resume_text):
    """
    Estimates if resume length is appropriate based on word count.
    """
    word_count = len(resume_text.split())
    
    if word_count < 150:
        return "Too Short", word_count
    elif word_count > 600:
        return "Too Long (consider trimming to 1 page)", word_count
    else:
        return "Good Length", word_count