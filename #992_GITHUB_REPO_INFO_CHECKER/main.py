import requests

def fetch_github_stats(username):
    user_api_url = f"https://api.github.com/users/{username}"
    user_response = requests.get(user_api_url)
    
    if user_response.status_code != 200:
        print(f"Error: Could not find user '{username}'. Status code: {user_response.status_code}")
        return

    user_data = user_response.json()
    followers = user_data.get('followers', 0)

    repos_api_url = f"https://api.github.com/users/{username}/repos"
    repos_response = requests.get(repos_api_url)
    
    if repos_response.status_code != 200:
        print(f"Error: Could not fetch repositories for '{username}'.")
        return

    repos_data = repos_response.json()

    print("\n" + "="*40)
    print(f"GitHub Stats for: {user_data.get('name', username)} (@{username})")
    print(f"Followers: {followers}")
    print("="*40)
    
    print("\nTop Repositories:")
    
    sorted_repos = sorted(repos_data, key=lambda x: x.get('stargazers_count', 0), reverse=True)
    
    if not sorted_repos:
        print("This user has no public repositories.")
    else:
        for repo in sorted_repos[:10]:
            repo_name = repo.get('name')
            stars = repo.get('stargazers_count')
            forks = repo.get('forks_count')
            print(f"- {repo_name:<30} ⭐ {stars:<5} | 🍴 {forks}")
    
    print("\n" + "="*40)

if __name__ == "__main__":
    github_username = input("Enter the GitHub username to check: ")
    if github_username:
        fetch_github_stats(github_username)
    else:
        print("Username cannot be empty.")