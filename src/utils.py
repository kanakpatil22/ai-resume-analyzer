def save_report(matched_skills, missing_skills, score, output_path="resume_report.txt"):
    """
    Saves the analysis result into a text file.
    """
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("===== RESUME ANALYSIS REPORT =====\n\n")
        
        file.write("Skills Found:\n")
        for skill in matched_skills:
            file.write(f"- {skill}\n")
        
        file.write("\nSkills Missing:\n")
        for skill in missing_skills:
            file.write(f"- {skill}\n")
        
        file.write(f"\nResume Score: {score}%\n")
    
    print(f"\n📄 Report saved to: {output_path}")