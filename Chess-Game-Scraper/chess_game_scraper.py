import requests

class ChessGameScraper:
    def __init__(self, player_username):
        self.player_username = player_username
        self.api_url = f"https://api.chess.com/pub/player/{player_username}/games"

    def get_recent_games(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json().get("games", [])
        else:
            print("Error retrieving games.")
            return []

    def display_game_info(self, game):
        print(f"\nGame ID: {game['id']}")
        print(f"White: {game['white']['username']} vs Black: {game['black']['username']}")
        print(f"Result: {game['status']}")
        print("Moves:", " ".join(game['moves']))
        print(f"Opening: {game.get('opening', 'Unknown opening')}")

def main():
    player_username = input("Enter your favorite chess player's username: ")
    scraper = ChessGameScraper(player_username)
    recent_games = scraper.get_recent_games()

    if recent_games:
        print(f"\nRecent games for {player_username}:")
        for game in recent_games:
            scraper.display_game_info(game)
    else:
        print("No recent games found.")

if __name__ == "__main__":
    main()
