import requests, argparse, textwrap, webbrowser, sys

HEADERS = {"User-Agent": "RedditTopViewer/1.0 (by script)"}

def fetch_top(sub="all", n=10, t="day"):
    url = f"https://www.reddit.com/r/{sub}/top/.json"
    params = {"limit": n, "t": t}
    r = requests.get(url, headers=HEADERS, params=params, timeout=10)
    if r.status_code != 200:
        raise SystemExit(f"Error: {r.status_code} fetching {url}")
    data = r.json()
    posts = []
    for item in data.get("data", {}).get("children", []):
        d = item["data"]
        posts.append({
            "title": d.get("title"),
            "score": d.get("score"),
            "author": d.get("author"),
            "url": d.get("url"),
            "comments": d.get("num_comments"),
            "permalink": "https://reddit.com" + d.get("permalink", "")
        })
    return posts

def pretty_print(posts, width=80):
    wrap = lambda s: "\n".join(textwrap.wrap(s, width=width))
    for i, p in enumerate(posts, 1):
        print(f"{i}. {wrap(p['title'])}")
        print(f"   score: {p['score']}  author: {p['author']}  comments: {p['comments']}")
        print(f"   link: {p['url']}")
        print(f"   comments: {p['permalink']}\n")

def main():
    ap = argparse.ArgumentParser(description="Reddit Top Posts Viewer (compact)")
    ap.add_argument("-s","--sub", default="all", help="subreddit (default: all)")
    ap.add_argument("-n","--num", type=int, default=10, help="number of posts (max 100)")
    ap.add_argument("-t","--timeframe", default="day", choices=["hour","day","week","month","year","all"])
    ap.add_argument("--width", type=int, default=80, help="wrap width")
    args = ap.parse_args()

    try:
        posts = fetch_top(args.sub, min(max(1, args.num), 100), args.timeframe)
    except Exception as e:
        print("Failed to fetch:", e)
        sys.exit(1)

    if not posts:
        print("No posts found.")
        return

    pretty_print(posts, width=args.width)

    #open a post's comments page
    try:
        sel = input("Open which post in browser? (number or Enter to quit) ").strip()
        if sel:
            i = int(sel)-1
            if 0 <= i < len(posts):
                webbrowser.open(posts[i]["permalink"])
    except (ValueError, KeyboardInterrupt):
        pass

if __name__ == "__main__":
    main()
