import re
import argparse

def format_text(text):
    # Remove multiple spaces and replace with single space
    text = re.sub(r'\s+', ' ', text)
    
    # Remove spaces before punctuation marks
    text = re.sub(r'\s+([.,!?])', r'\1', text)
    
    # Ensure single space after punctuation marks
    text = re.sub(r'([.,!?])\s*', r'\1 ', text)
    
    # Split text into sentences
    sentences = re.split(r'([.!?])\s+', text)
    
    # Capitalize first letter of each sentence
    formatted_text = ''
    for i in range(0, len(sentences)-1, 2):
        sentence = sentences[i].strip()
        if sentence:
            # Capitalize first letter of the sentence
            sentence = sentence[0].upper() + sentence[1:] if len(sentence) > 1 else sentence.upper()
            formatted_text += sentence + sentences[i+1] + ' '
    
    # Handle the last sentence if it exists
    if len(sentences) % 2 == 1:
        last_sentence = sentences[-1].strip()
        if last_sentence:
            last_sentence = last_sentence[0].upper() + last_sentence[1:] if len(last_sentence) > 1 else last_sentence.upper()
            formatted_text += last_sentence
    
    return formatted_text.strip()

def process_file(input_path, output_path=None):
    try:
        # Read input file
        with open(input_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Format the text
        formatted_text = format_text(text)
        
        # Write to output file or overwrite input file
        output_file = output_path if output_path else input_path
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(formatted_text)
        
        print(f"Text has been formatted and saved to: {output_file}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Auto Text Formatter: Clean extra spaces and capitalize sentences.')
    parser.add_argument('input_file', help='Path to the input text file')
    parser.add_argument('-o', '--output', help='Path to the output file (optional)')
    
    args = parser.parse_args()
    process_file(args.input_file, args.output)

if __name__ == "__main__":
    main()