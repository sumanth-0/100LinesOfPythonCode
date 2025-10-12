# Random Movie Picker 🎬🍿

A simple Python CLI tool that randomly selects a movie from a list to help you decide what to watch tonight!

## Features

- 🎯 Randomly picks a movie from a list
- 📁 Load movies from a text file (one movie per line)
- 📝 Uses a built-in default list of popular movies if no file is provided
- 🎨 Displays results with fun emojis

## Usage

### Using the default movie list:

```bash
python random_movie_picker.py
```

### Using a custom movie list from a file:

```bash
python random_movie_picker.py movies.txt
```

### Example movie list file format (movies.txt):

```
The Shawshank Redemption
The Godfather
The Dark Knight
Pulp Fiction
Inception
Interstellar
```

## How It Works

1. The script accepts an optional command-line argument for a text file containing movie names
2. If no file is provided, it uses a built-in list of 15 popular movies
3. The script randomly selects one movie from the list
4. Displays the selected movie with emoji decorations

## Requirements

- Python 3.x
- No external dependencies required (uses only standard library)

## Example Output

```
🎬 Random Movie Picker 🍿

📝 Using default movie list...

🎯 Total movies available: 15

==================================================

🌟 Tonight's movie suggestion: Inception 🌟

==================================================

🍿 Enjoy your movie! 🎬
```

## Contributing

Feel free to contribute by:
- Adding more default movies
- Improving the CLI interface
- Adding new features

## License

This project is part of the 100 Lines of Python Code repository.
