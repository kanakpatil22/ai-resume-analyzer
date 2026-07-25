from src.config import SKILLS_LIST, RESUME_ELEMENTS, AI_PHRASES

def find_skills(resume_text, skills_list=SKILLS_LIST):
    """
    Checks which skills from the given skills_list are present in the resume text.
    Returns two lists: matched skills and missing skills.
    """
    resume_text_lower = resume_text.lower()
    
    matched_skills = []
    missing_skills = []
    
    for skill in skills_list:
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

def detect_ai_phrases(resume_text):
    """
    Scans resume text for common AI-sounding / cliché phrases and 
    suggests more natural alternatives. This is a heuristic check based 
    on commonly overused phrases — not a definitive AI-detection tool.
    """
    
    
    resume_text_lower = resume_text.lower()
    
    flagged_phrases = []
    
    for phrase, suggestion in AI_PHRASES.items():
        if phrase in resume_text_lower:
            flagged_phrases.append((phrase, suggestion))
    
    total_checked = len(AI_PHRASES)
    ai_likelihood = round((len(flagged_phrases) / total_checked) * 100, 2) if total_checked > 0 else 0
    
    return flagged_phrases, ai_likelihood

def generate_improvement_suggestions(missing_skills, missing_elements, score):
    """
    Generates a prioritized, actionable list of suggestions to improve 
    the resume based on missing skills and missing elements.
    """
    suggestions = []
    
    if missing_skills:
        top_skills = missing_skills[:5]
        skills_text = ", ".join(top_skills)
        suggestions.append(
            f"Add these skills if you have them: {skills_text}. "
            f"This can directly boost your score."
        )
    
    element_messages = {
        "internship": "Add any internship experience, even short-term or unpaid ones.",
        "certification": "List any certifications you've completed (even free online courses count).",
        "certified": "List any certifications you've completed (even free online courses count).",
        "project": "Include 2-3 projects with a short description of what you built and the tools used.",
        "achievement": "Mention any achievements or awards, academic or extracurricular.",
        "award": "Mention any achievements or awards, academic or extracurricular.",
        "linkedin": "Add your LinkedIn profile link — recruiters often check it.",
        "github": "Add your GitHub link if you have coding projects to showcase.",
        "portfolio": "Add a portfolio link if you have one (especially for design/dev roles).",
        "summary": "Add a 2-3 line summary at the top describing who you are professionally.",
        "objective": "Add a 2-3 line summary at the top describing who you are professionally.",
        "volunteer": "Mention any volunteer work — it shows initiative and teamwork.",
    }
    
    for element in missing_elements:
        if element in element_messages:
            suggestions.append(element_messages[element])
    
    if score < 40:
        priority_message = "Priority: Focus on adding the missing skills above first — they have the biggest impact on your score."
    elif score < 70:
        priority_message = "Priority: You're doing well! Adding a couple more skills and missing sections will push your score higher."
    else:
        priority_message = "Priority: Your resume is strong. Focus on polishing wording and adding any remaining missing sections."
    
    return suggestions, priority_message