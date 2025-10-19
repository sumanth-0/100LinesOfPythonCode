import requests

def get_repo_info(owner, repo):
    """Fetch repository info from GitHub API."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch repo info. HTTP {response.status_code}")
    
    data = response.json()
    return {
        "name": data.get("full_name", "N/A"),
        "stars": data.get("stargazers_count", 0),
        "forks": data.get("forks_count", 0),
        "open_issues": data.get("open_issues_count", 0)
    }

def main():
    print("=== GitHub Repository Info ===")
    owner = input("Enter repo owner (username/org): ").strip()
    repo = input("Enter repo name: ").strip()
    
    try:
        info = get_repo_info(owner, repo)
        print(f"\nRepository: {info['name']}")
        print(f"⭐ Stars: {info['stars']}")
        print(f"🍴 Forks: {info['forks']}")
        print(f"🐛 Open Issues: {info['open_issues']}\n")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
