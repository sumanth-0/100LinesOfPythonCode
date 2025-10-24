import requests

# Fetch response (tech news only, for now).
response = requests.get("https://saurav.tech/NewsAPI/top-headlines/category/technology/in.json")

# Check for success.
if response.status_code == 200:
    # Keep only the top 5 articles. (Assumes that more than 5 are fetched, adding a check for that would be unnecessary for now.)
    articles = response.json()["articles"][:5]
    
    # Filter the data. Quite ugly, I know, but I like conciseness 😅
    articles = map(lambda x: f"{x[0]+1}. {x[1]["title"]}", enumerate(articles))
    print("The Top 5 News Headlines are:")
    print(*articles, sep="\n\n")
else:
    print(f"Error: {response.status_code}")