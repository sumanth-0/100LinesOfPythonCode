# Caesar Cipher Hacker

This Python script is designed to decode messages encrypted with the Caesar cipher by analyzing the text and determining the best shift value for decryption. It utilizes the Natural Language Toolkit (nltk) to evaluate the decoded messages based on recognized English words.

## Features

- Decodes Caesar cipher messages with varying shift values.
- Automatically identifies the best shift for readability, thus cracking the shift value
- Can work with text input or read from a specified file.

## Requirements

Before running the script, you need to set up the environment:

1. **Install Dependencies**: Ensure you have the required Python packages by running:
   ```bash
   pip install nltk
   ```
2. **Download NLTK Resources**: Run `download_nltk_resources.py` to download necessary NLTK data files. 

## Usage

1. Ensure you've completed the setup steps above.
2. You can either:
   - Edit the `encoded_file.txt` to include your encoded message, or specify the file to be used (it can be a large text file).
   - Or, input the encoded text directly when prompted.

3. Run the script with:
   ```bash
   python cipherhacker.py
   ```

4. Follow the prompts:
   - Enter `file` to read from `encoded_file.txt`(default) or any other file.
   - Enter `text` to input the encoded message directly.

## Output

The script will display:
- The shift value used for encoding.
- The decoded message for the provided ciphertext.

## Example

To decode a message:
1. Place your encoded text in `encoded_file.txt` or input any other txt file or have a sample ready to input.
2. Run the script and follow the prompts.
