import requests
import random

# LeetCode GraphQL endpoint
API_URL = "https://leetcode.com/graphql"
# Query to get problems by difficulty
QUERY = """
query getRandomProblem($difficulty: String!) {
  problemsetQuestionList(
    categorySlug: "algorithms"
    filters: { difficulty: $difficulty }
    limit: 50
    skip: 0
  ) {
    questions {
      title
      titleSlug
      difficulty
    }
  }
}
"""

# Headers to mimic a browser request
HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com/problemset/all/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_random_problem_link(difficulty):
    """Fetches a random problem link from LeetCode by difficulty."""
    response = requests.post(API_URL, json={"query": QUERY, "variables": {"difficulty": difficulty}}, headers=HEADERS)
    
    if response.status_code != 200:
        return f"Failed to fetch problems (status code: {response.status_code})"

    questions = response.json().get("data", {}).get("problemsetQuestionList", {}).get("questions", [])
    if not questions:
        return "No problems found for the given difficulty."

    # Select a random problem
    random_problem = random.choice(questions)
    problem_title = random_problem.get("title")
    problem_slug = random_problem.get("titleSlug")
    
    # Return problem title and link
    return f"{problem_title}: https://leetcode.com/problems/{problem_slug}"

if __name__ == "__main__":
    # Example usage with random difficulty level
    difficulties = ["EASY", "MEDIUM", "HARD"]
    selected_difficulty = random.choice(difficulties)
    print(f"Fetching a random {selected_difficulty} problem...")
    print(get_random_problem_link(selected_difficulty))
