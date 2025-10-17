#!/usr/bin/env python3
"""
Daily Joke Fetcher (compact version)
- Fetches a joke daily from public APIs
- Caches per day (~/.cache/daily_joke.json)
- PEP 8 compliant, <100 lines
"""
from datetime import date
import json, os, sys
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

CACHE = os.path.join(os.path.expanduser("~"), ".cache", "daily_joke.json")
API_URLS = [
    "https://official-joke-api.appspot.com/jokes/random",
    "https://v2.jokeapi.dev/joke/Any?format=json"
]

def ensure_dir(path):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)

def fetch_json(url):
    req = Request(url, headers={"User-Agent": "daily-joke/1.0"})
    with urlopen(req, timeout=5) as r:
        return json.load(r)

def normalize_joke(d):
    if "setup" in d: return d["setup"], d["punchline"]
    if d.get("type")=="single": return "", d["joke"]
    if d.get("type")=="twopart": return d.get("setup",""), d.get("delivery","")
    for k in ("joke","text"): 
        if k in d: return "", d[k]
    raise ValueError("Unknown joke format")

def fetch_joke():
    for url in API_URLS:
        try: return normalize_joke(fetch_json(url))
        except: continue
    raise RuntimeError("Failed to fetch joke")

def load_cache():
    try:
        with open(CACHE,"r") as f:
            j = json.load(f)
        if j.get("date")==date.today().isoformat(): return j.get("headline",""), j.get("punchline","")
    except: return None

def save_cache(headline,punchline):
    ensure_dir(CACHE)
    with open(CACHE,"w") as f:
        json.dump({"date":date.today().isoformat(),"headline":headline,"punchline":punchline}, f)

def print_joke(h,p): 
    if h: print(h,"\n"+ "-"*max(10,len(h)))
    print(p)

def main():
    force = "--force" in sys.argv
    if not force:
        c = load_cache()
        if c: return print_joke(*c)
    try: h,p = fetch_joke()
    except RuntimeError as e: print(e, file=sys.stderr); sys.exit(1)
    print_joke(h,p)
    try: save_cache(h,p)
    except: pass

if __name__=="__main__": main()
