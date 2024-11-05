import json

def create_resume():
    resume = {}
    resume['name'] = input("Enter your name: ")
    resume['email'] = input("Enter your email: ")
    resume['phone'] = input("Enter your phone number: ")
    resume['address'] = input("Enter your address: ")
    resume['summary'] = input("Enter a brief summary of your skills and experience: ")

    # Education section
    num_educations = int(input("Enter the number of educational qualifications: "))
    resume['education'] = []
    for i in range(num_educations):
        education = {}
        education['degree'] = input(f"Enter degree {i+1}: ")
        education['institution'] = input(f"Enter institution {i+1}: ")
        education['year'] = input(f"Enter year of completion {i+1}: ")
        education['cgpa'] = float(input(f"Enter CGPA {i+1}: "))
        resume['education'].append(education)

    # Experience section
    num_experiences = int(input("Enter the number of work experiences: "))
    resume['experience'] = []
    for i in range(num_experiences):
        experience = {}
        experience['title'] = input(f"Enter job title {i+1}: ")
        experience['company'] = input(f"Enter company name {i+1}: ")
        experience['start_date'] = input(f"Enter start date {i+1} (YYYY-MM-DD): ")
        experience['end_date'] = input(f"Enter end date {i+1} (YYYY-MM-DD): ")
        experience['description'] = input(f"Enter job description {i+1}: ")
        resume['experience'].append(experience)

    # Skills section
    skills = input("Enter your skills (comma-separated): ").split(',')
    resume['skills'] = [skill.strip() for skill in skills]

    # Projects section
    num_projects = int(input("Enter the number of projects: "))
    resume['projects'] = []
    for i in range(num_projects):
        project = {}
        project['title'] = input(f"Enter project title {i+1}: ")
        project['description'] = input(f"Enter project description {i+1}: ")
        project['link'] = input(f"Enter project link {i+1}: ")
        resume['projects'].append(project)

    with open('resume.json', 'w') as f:
        json.dump(resume, f, indent=4)
    print("Resume created successfully!")

if __name__ == '__main__':
    create_resume()
