# 📊 GitHub User Stats Viewer

A command-line tool that fetches and displays public statistics for any GitHub user. Enter a username, and the script will show you their follower count and a list of their top public repositories, sorted by stars.

This script uses the official GitHub API to retrieve real-time data.

## ✨ Features

-   **Follower Count**: Displays the total number of followers for the user.
-   **Top Repositories**: Lists the user's top 10 public repositories, sorted by star count.
-   **Repo Stats**: Shows the number of stars ⭐ and forks 🍴 for each repository.
-   **User-Friendly**: Simple prompt-based interface.

## ⚙️ Setup

1.  **Prerequisites**: Make sure you have **Python 3.x** installed.

2.  **Install the library**:
    This project requires the `requests` library. Install it using pip:
    ```bash
    pip install requests
    ```

## 🚀 Usage

To run the script, execute the following command in your terminal:

```bash
python main.py