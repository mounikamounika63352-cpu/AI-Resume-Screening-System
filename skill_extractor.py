import pandas as pd

def extract_skills(resume_text):

    skills_df = pd.read_csv("data/skills.csv")

    skill_list = skills_df["Skill"].tolist()

    detected = []

    resume_text = resume_text.lower()

    for skill in skill_list:
        if skill.lower() in resume_text:
            detected.append(skill)

    return sorted(list(set(detected)))