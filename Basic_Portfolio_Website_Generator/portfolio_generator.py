def generate_portfolio(name, skills, projects):
    """Generate a basic HTML portfolio page."""
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}'s Portfolio</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }}
        h1 {{ color: #333; }}
        ul {{ list-style-type: none; }}
        .skills, .projects {{ margin-top: 20px; }}
    </style>
</head>
<body>
    <h1>Welcome to {name}'s Portfolio</h1>
    <h2>Skills</h2>
    <ul class="skills">{''.join(f'<li>{skill}</li>' for skill in skills)}</ul>
    <h2>Projects</h2>
    <ul class="projects">{''.join(f'<li>{project}</li>' for project in projects)}</ul>
</body>
</html>"""

    with open("portfolio.html", "w") as file:
        file.write(html_content)
    
    print("Portfolio generated! Open 'portfolio.html' to view it.")

def main():
    name = input("Enter your name: ")
    skills = input("Enter your skills (comma-separated): ").split(',')
    projects = input("Enter your projects (comma-separated): ").split(',')
    
    # Stripping whitespace
    skills = [skill.strip() for skill in skills]
    projects = [project.strip() for project in projects]
    
    generate_portfolio(name, skills, projects)

if __name__ == "__main__":
    main()
