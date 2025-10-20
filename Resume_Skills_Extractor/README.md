# Resume Skills Extractor 📄

A lightweight NLP-based Python tool that extracts technical and soft skills from resumes in multiple formats (PDF, DOCX, TXT) using intelligent keyword matching.

## Features ✨

- 📑 Supports multiple file formats (PDF, DOCX, TXT)
- 🔍 Extracts 40+ technical skills (Python, Java, React, AWS, etc.)
- 🤝 Identifies 15+ soft skills (Leadership, Communication, etc.)
- 📧 Extracts contact information (email, phone)
- 🎯 Uses regex pattern matching for accurate detection
- 💾 Clean, modular code under 100 lines

## Requirements 📋

pip install PyPDF2 python-docx


## Usage 🚀

Run the script:

python resume_skills_extractor.py

text

Enter the path to your resume file when prompted:

📁 Enter resume file path (PDF/DOCX/TXT): sample_resume.pdf
## Example Output 📊

==============================================================
📄 RESUME SKILLS EXTRACTOR
📁 Enter resume file path (PDF/DOCX/TXT): john_doe_resume.pdf

🔍 Analyzing resume...

📋 File: john_doe_resume.pdf
📧 Email: john.doe@email.com
📱 Phone: +1-234-567-8900

💼 Technical Skills Found (12):

Python

Django

React

PostgreSQL

Docker

AWS

Git

FastAPI

MongoDB

Jenkins

Kubernetes

Machine Learning

🤝 Soft Skills Found (5):

Leadership

Communication

Problem Solving

Teamwork

Analytical


### Batch Processing

Modify the main function to process multiple files:

import os

resume_folder = "path/to/resumes"
for filename in os.listdir(resume_folder):
if filename.endswith(('.pdf', '.docx', '.txt')):
result = analyze_resume(os.path.join(resume_folder, filename))
print(result)


## Use Cases 🎯

- **HR Recruitment**: Quickly screen candidate resumes
- **Job Matching**: Match candidate skills with job requirements
- **Resume Analysis**: Identify skill gaps in applicants
- **Portfolio Building**: Extract skills for personal branding
- **ATS Systems**: Integrate into Applicant Tracking Systems

## Limitations ⚠️

- Keyword-based matching (not semantic understanding)
- Requires skills to be explicitly mentioned
- May miss context-specific skills or abbreviations
- PDF extraction quality depends on document formatting

## Future Enhancements 🚀

- Add semantic similarity using NLP models (spaCy, BERT)
- Extract work experience and education details
- Support for more file formats (HTML, RTF)
- Web interface with file upload
- Export results to JSON/CSV

## License 📄

MIT License - Feel free to use and modify!

## Contributing 🤝

Part of the 100LinesOfPythonCode repository. Contributions welcome!
File Structure
text
Resume_Skills_Extractor/
├── resume_skills_extractor.py
└── README.md
