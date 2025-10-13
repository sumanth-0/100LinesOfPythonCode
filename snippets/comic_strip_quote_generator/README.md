# Comic Strip Quote Generator

Generate fun comic strips with random quotes overlaid on colorful cartoon-style images!

## Description

This Python script creates comic-style images with random humorous quotes. It uses the Pillow (PIL) library to:
- Generate colorful cartoon-style backgrounds with random shapes
- Overlay quotes with comic-style text formatting
- Add text outlines for better readability
- Automatically wrap text to fit the image

## Requirements

```bash
pip install Pillow
```

## Usage

```bash
python comic_strip_quote_generator.py
```

The script will:
1. Create an `output` directory if it doesn't exist
2. Generate a random cartoon-style background
3. Select a random quote from the built-in collection
4. Overlay the quote with comic-style formatting
5. Save the result as `comic_quote_XXXX.png` in the output folder

## Sample Quotes

The script includes fun quotes like:
- "With great power comes great responsibility!"
- "Error 404: Motivation not found"
- "Keep calm and code on!"
- "There's no place like 127.0.0.1"
- And more!

## Customization

You can easily customize:
- Add your own quotes to the `QUOTES` list
- Modify image dimensions in `create_sample_image()`
- Change font size in `add_quote_to_image()`
- Adjust colors and background elements

## Features

- Random colorful backgrounds
- Automatic text wrapping
- Comic-style text with outlines
- Simple one-command execution
- Under 100 lines of code!

## Example Output

Each run generates a unique comic with:
- Random background colors
- Random decorative shapes
- A randomly selected quote
- Professional comic-style text formatting

## License

Feel free to use and modify this script for your projects!

---

**Part of the 100 Lines of Python Code project** 🚀
