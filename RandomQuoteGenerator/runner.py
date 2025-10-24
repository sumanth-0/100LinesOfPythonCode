import requests
import json
import os
import ssl
import urllib3
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align
from rich.box import DOUBLE
from pyfiglet import Figlet

# Disable SSL verification globally
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

console = Console()
SAVE_FILE = "saved_quotes.json"

def fetch_quote():
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()
        data = response.json()
        return data["content"], data["author"]
    except requests.RequestException as e:
        console.print(f"[red]Error fetching quote:[/red] {e}")
        return None, None

def display_heading(text):
    figlet = Figlet(font="slant")
    console.print(Align.center(f"[bold white]{figlet.renderText(text)}"))

def display_quote(quote, author):
    panel = Panel(
        Align.center(f"[italic]{quote}[/italic]\n\n— [bold]{author}[/bold]"),
        title="[bold blue]Quote[/bold blue]",
        border_style="cyan",
        box=DOUBLE,
        padding=(1, 2)
    )
    console.print(panel)

def save_quote(quote, author):
    saved = []
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            saved = json.load(f)
    saved.append({"content": quote, "author": author})
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saved, f, indent=2)
    console.print("[green]Quote saved successfully.[/green]")

def view_saved_quotes():
    if not os.path.exists(SAVE_FILE):
        console.print("[red]No saved quotes found.[/red]")
        return
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        saved = json.load(f)
    if not saved:
        console.print("[red]No saved quotes yet.[/red]")
        return

    console.print("\n[bold]Saved Quotes:[/bold]\n")
    for i, q in enumerate(saved, 1):
        panel = Panel(
            f"[italic]{q['content']}[/italic]\n\n— [bold]{q['author']}[/bold]",
            title=f"Quote {i}",
            border_style="blue",
            padding=(1, 2),
            box=DOUBLE,
        )
        console.print(i,q)
        console.print(panel)

def main():
    display_heading("Random Quote Generator")
    current_quote, current_author = fetch_quote()
    display_quote(current_quote, current_author)
    while True:

        action = Prompt.ask(
            "Options: [bold]save[/bold], [bold]next[/bold], [bold]view[/bold], [bold]exit[/bold]",
            choices=["save", "next", "view", "exit"],
            default="next"
        )

        if action == "save":
            save_quote(current_quote, current_author)
        elif action == "view":
            view_saved_quotes()
            # Do NOT redisplay current quote; just continue loop
            continue
        elif action == "next":
            current_quote, current_author = fetch_quote()
            display_quote(current_quote, current_author)
        elif action == "exit":
            console.print("\n[bold]Goodbye![/bold]")
            break

if __name__ == "__main__":
    main()
