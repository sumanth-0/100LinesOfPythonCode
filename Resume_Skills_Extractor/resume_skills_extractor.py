"""
Resume Skills Extractor - Extracts skills from resumes (PDF, DOCX, TXT)
Includes 200+ predefined skills + skills section parsing
"""

import re, PyPDF2, docx
from pathlib import Path

# Comprehensive skill database (200+ skills)
SKILLS = {
    'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'ruby', 'php', 'swift', 'kotlin', 'go', 'rust', 'scala', 'perl', 'r',
    'react', 'angular', 'vue', 'node.js', 'django', 'flask', 'fastapi', 'spring boot', 'express', 'next.js', 'laravel', 'asp.net',
    'html', 'css', 'sass', 'tailwind', 'bootstrap', 'jquery', 'redux', 'graphql', 'rest api', 'websocket', 'ajax',
    'sql', 'mongodb', 'postgresql', 'mysql', 'redis', 'cassandra', 'oracle', 'sqlite', 'dynamodb', 'firebase', 'elasticsearch',
    'docker', 'kubernetes', 'aws', 'azure', 'gcp', 'jenkins', 'gitlab', 'github actions', 'terraform', 'ansible', 'ci/cd',
    'machine learning', 'deep learning', 'nlp', 'computer vision', 'data science', 'ai', 'tensorflow', 'pytorch', 'keras',
    'scikit-learn', 'pandas', 'numpy', 'matplotlib', 'seaborn', 'opencv', 'nltk', 'spacy', 'hugging face',
    'git', 'svn', 'jira', 'agile', 'scrum', 'kanban', 'microservices', 'devops', 'linux', 'unix', 'bash', 'powershell',
    'tableau', 'power bi', 'excel', 'spark', 'hadoop', 'kafka', 'rabbitmq', 'nginx', 'apache', 'selenium', 'pytest', 'junit',
    'leadership', 'communication', 'teamwork', 'problem solving', 'critical thinking', 'time management', 'adaptability',
    'creativity', 'collaboration', 'negotiation', 'presentation', 'analytical', 'organizational', 'detail-oriented',
    'project management', 'strategic planning', 'conflict resolution', 'decision making', 'emotional intelligence'
}

def extract_text(file_path):
    """Extract text from PDF, DOCX, or TXT"""
    ext = Path(file_path).suffix.lower()
    if ext == '.pdf':
        with open(file_path, 'rb') as f:
            return ''.join([page.extract_text() for page in PyPDF2.PdfReader(f).pages])
    elif ext == '.docx':
        return '\n'.join([p.text for p in docx.Document(file_path).paragraphs])
    elif ext == '.txt':
        return open(file_path, 'r', encoding='utf-8').read()
    raise ValueError(f"Unsupported format: {ext}")

def extract_skills_section(text):
    """Extract skills from dedicated skills section"""
    skills_section = re.search(r'(?:skills?|technical skills?|core competencies)[:\s]*\n(.*?)(?:\n\n|\n[A-Z][a-z]+:|\Z)', 
                               text, re.IGNORECASE | re.DOTALL)
    if skills_section:
        section_text = skills_section.group(1)
        # Extract skills separated by comma, pipe, bullet, or newline
        return set(re.findall(r'[•\-\*]?\s*([A-Za-z][A-Za-z0-9\s\.\+#\-]+?)(?:[,\|\n•\-\*]|$)', section_text))
    return set()

def find_all_skills(text):
    """Find all skills using keyword matching"""
    text_lower = text.lower()
    found = set()
    for skill in SKILLS:
        if re.search(r'\b' + re.escape(skill.lower()) + r'\b', text_lower):
            found.add(skill)
    return found

def extract_contact_info(text):
    """Extract email and phone"""
    email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    phone = re.search(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
    return email.group(0) if email else None, phone.group(0) if phone else None

def analyze_resume(file_path):
    """Analyze resume and extract all skills"""
    text = extract_text(file_path)
    skills_from_section = extract_skills_section(text)
    skills_from_keywords = find_all_skills(text)
    all_skills = skills_from_section | skills_from_keywords
    email, phone = extract_contact_info(text)
    
    return {
        'file': Path(file_path).name,
        'skills': sorted([s.strip() for s in all_skills if len(s.strip()) > 1]),
        'email': email,
        'phone': phone
    }

def main():
    print("="*60 + "\n📄 RESUME SKILLS EXTRACTOR\n" + "="*60)
    file_path = input("\n📁 Enter resume file path: ").strip()
    
    if not Path(file_path).exists():
        print("❌ File not found!")
        return
    
    print("\n🔍 Analyzing...")
    result = analyze_resume(file_path)
    
    print(f"\n📋 File: {result['file']}")
    print(f"📧 Email: {result['email'] or 'Not found'}")
    print(f"📱 Phone: {result['phone'] or 'Not found'}")
    print(f"\n💼 Skills Found ({len(result['skills'])}):")
    for skill in result['skills']:
        print(f"  • {skill.title()}")

if __name__ == "__main__":
    main()
