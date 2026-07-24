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

def compare_with_job_description(resume_text, job_description_text):
    """
    Compares resume against a job description by checking which words 
    from the job description also appear in the resume.
    """
    resume_text_lower = resume_text.lower()
    
    common_words_to_ignore = {
        "the", "and", "for", "with", "you", "are", "will", "our",
        "have", "has", "this", "that", "your", "from", "who", "can",
        "job", "work", "role", "team", "years", "experience", "skills",
        "a", "an", "of", "in", "to", "is", "as", "on", "at", "be"
    }
    
    job_words = job_description_text.lower().replace(",", " ").replace(".", " ").split()
    unique_job_keywords = set(word for word in job_words if len(word) > 2 and word not in common_words_to_ignore)
    
    matched_keywords = []
    missing_keywords = []
    
    for keyword in unique_job_keywords:
        if keyword in resume_text_lower:
            matched_keywords.append(keyword)
        else:
            missing_keywords.append(keyword)
    
    total = len(matched_keywords) + len(missing_keywords)
    match_percentage = round((len(matched_keywords) / total) * 100, 2) if total > 0 else 0
    
    return matched_keywords, missing_keywords, match_percentage