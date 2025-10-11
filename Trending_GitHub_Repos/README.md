<div align="center">
  <h1>Trending GitHub Repositories</h1>
  <p>Aggregate trending GitHub repositories and display in a aesthetic terminal output.</p>
</div>

This script intakes trending GitHub repositories using the `gtrending` package, allowing the user to specify the number of repositories to pull from the trending section, starting with the most popular and descending down.

## Dependencies

```bash
pip3 install gtrending rich
```

## Usage

This script comes with an optional argument where you can choose the number of repositories to return from the trending page:

```bash
python3 trending_github_repos.py -r 10
```

NOTE: Change the `10` to your desired integer.

If you just want to use the default (`10`), don't pass any arguments:
```bash
python3 trending_github_repos.py
```
