import shutil
import argparse
from typing import List, Dict

from gtrending import fetch_repos
from rich.text import Text
from rich.rule import Rule
from rich.table import Table
from rich.panel import Panel
from rich.console import Console

parser = argparse.ArgumentParser(description="Get a list of the trending repositories on GitHub!")
parser.add_argument("-r", "--repos", help="Choose the number of GitHub repositories to pull from the trending page", default=10)
args = parser.parse_args()

class TrendingGitHubRepos():
    def make_repo_panel(self, repo: Dict, panel_width: int) -> Panel:
        """
        Creates individual repo panels where all of the repo information is stored and styled
        """
        repo_name = f"[bold]{repo['fullname']}[bold]"
        repo_stars = f"⭐ Stars: {repo.get('stars', 0)}"
        repo_forks = f"🍴 Forks: {repo.get('forks', 0)}"
        repo_url = f"[link={repo['url']}]🔗 View on GitHub[/link]"

        # We strip the whitespace before pushing to Text() body
        get_repo_desc = repo.get("description") or "No description found."
        repo_description = f"Description: {get_repo_desc.strip()}"

        body = Text(no_wrap=False)
        body.append(f"{repo_description}\n\n", style="bold")
        body.append(f"{repo_stars}\n", style="bold yellow")
        body.append(f"{repo_forks}", style="bold cyan")

        return Panel(
            body,
            subtitle=repo_url,
            title=repo_name,
            width=panel_width,
            border_style="bright_red",
            padding=(1, 1),
            expand=True,
        )

    def main(self):
        console = Console()

        # We do our best to maintain a consistent width based on the width of the terminal and the number of columns created
        # Since the limit is set to 10, we chose 2 columns to keep it even
        # Since we chose 2 columns, each panel is set to "half the terminal" - gutter (2)
        panel_width = max(38, (shutil.get_terminal_size((100, 20)).columns - 2) // 2)

        console.print(Rule(f"🔥 [bold blue]Top {args.repos} Trending GitHub Repositories[/bold blue] 🔥"))

        # Fetch the top 10 current trending GitHub repos
        repos: List[Dict] = fetch_repos(language=None, since="daily")[:int(args.repos)]

        # As we create the panels, make sure both columns are locked to the same width
        table = Table(box=None, show_header=False, show_lines=False)
        table.add_column(no_wrap=True, min_width=panel_width, width=panel_width, max_width=panel_width)
        table.add_column(no_wrap=True, min_width=panel_width, width=panel_width, max_width=panel_width)

        row_cells = []

        for repo in repos:
            row_cells.append(self.make_repo_panel(repo, panel_width))

            # When a row has exactly 2 panels, we add that row to the table
            # Then we reset the row, so the next pair can be introduced
            if len(row_cells) == 2:
                table.add_row(*row_cells)
                row_cells = []

        # If there's not an even number of repos, we have a fallback to show the last one on it's own row
        if row_cells:
            while len(row_cells) < 2:
                row_cells.append(Text(""))

            table.add_row(*row_cells)

        console.print(table)

if __name__ == "__main__":
    TrendingGitHubRepos().main()
