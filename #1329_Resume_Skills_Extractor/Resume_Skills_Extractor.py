import re

#Defining a list of skills(more can be added)
SKILL_KEYWORDS = [
    "python", "java", "c", "c++", "javascript", "typescript", "html", "css",
    "react", "next.js", "node.js", "django", "flask", "rest api", "graphql",
    "sql", "mysql", "postgresql", "sqlite", "mongodb",
    "git", "github", "docker", "kubernetes", "aws", "azure", "gcp",
    "machine learning", "deep learning", "nlp", "computer vision",
    "pandas", "numpy", "matplotlib", "scikit-learn", "tensorflow", "pytorch",
    "excel", "tableau", "power bi", "data analysis", "data visualization"
]

def extract_skills(resume_text: str):
    
    resume_text = resume_text.lower() #lowercase for uniformity

    resume_text = re.sub(r'[^\w\s\+\#\.]', ' ', resume_text)

    found = set()
    for skill in SKILL_KEYWORDS:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, resume_text):
            found.add(skill)
    return sorted(found)

if __name__ == "__main__":
    #Example input
    sample_resume = """
    Skilled in Python, Machine Learning, Deep Learning,
    and Data Visualization using Tableau and Power BI. Hands-on experience with
    Django REST framework, SQL, and AWS cloud deployment.
    """
    skills = extract_skills(sample_resume)
    print("Extracted Skills:", skills)
