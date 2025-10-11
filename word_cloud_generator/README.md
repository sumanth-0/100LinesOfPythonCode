# Word Cloud Generator

A Python script to generate beautiful word cloud visualizations from text input using the `wordcloud` and `matplotlib` libraries.

## Features

- **Flexible Input**: Accept text from files or direct string input
- **Customizable Appearance**: Configure width, height, background color, and colormap
- **Output Options**: Save as image file or display interactively
- **Command-line Interface**: Easy-to-use CLI with multiple options
- **Under 100 Lines**: Clean, readable code in less than 100 lines

## Installation

Install the required dependencies:

```bash
pip install wordcloud matplotlib
```

## Usage

### Basic Usage

Generate a word cloud from a text file:

```bash
python word_cloud_generator.py input.txt
```

### Save to File

Generate and save the word cloud to an image file:

```bash
python word_cloud_generator.py input.txt -o wordcloud.png
```

### Using Direct Text Input

Generate from a text string:

```bash
python word_cloud_generator.py "Python is awesome for data visualization"
```

### Custom Dimensions

Specify custom width and height:

```bash
python word_cloud_generator.py input.txt -w 1200 -ht 600 -o large_wordcloud.png
```

### Custom Colors

Change background color and colormap:

```bash
python word_cloud_generator.py input.txt -bg black -c plasma -o dark_wordcloud.png
```

## Command-line Options

| Option | Short | Description | Default |
|--------|-------|-------------|--------|
| `--output` | `-o` | Output image file path | Display interactively |
| `--width` | `-w` | Width of word cloud | 800 |
| `--height` | `-ht` | Height of word cloud | 400 |
| `--background` | `-bg` | Background color | white |
| `--colormap` | `-c` | Matplotlib colormap | viridis |

## Examples

### Example 1: Default Settings
```bash
python word_cloud_generator.py sample.txt
```
Displays an interactive word cloud with default settings.

### Example 2: High-Resolution Export
```bash
python word_cloud_generator.py article.txt -w 1920 -ht 1080 -o high_res.png
```
Generates a high-resolution word cloud suitable for presentations.

### Example 3: Dark Theme
```bash
python word_cloud_generator.py data.txt -bg black -c hot -o dark_theme.png
```
Creates a word cloud with black background and "hot" colormap.

## Available Colormaps

Some popular matplotlib colormaps:
- `viridis` (default)
- `plasma`
- `inferno`
- `magma`
- `coolwarm`
- `rainbow`
- `hot`
- `cool`

## Requirements

- Python 3.6+
- wordcloud
- matplotlib

## License

This project is part of the 100 Lines of Python Code repository.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Issue Reference

Fixes #683
