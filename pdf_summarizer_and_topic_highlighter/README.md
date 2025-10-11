# PDF Summarizer & Topic Highlighter

## Description

A powerful tool to summarize PDF content and highlight key topics using Natural Language Processing (NLP). This tool is particularly helpful for students and researchers who need to quickly understand the main content and key topics of lengthy PDF documents.

## Features

- **PDF Text Extraction**: Extracts text content from PDF files using PyPDF2
- **Smart Summarization**: Generates concise summaries based on sentence scoring algorithm
- **Topic Highlighting**: Identifies and highlights the most frequent key topics
- **Stop Word Filtering**: Filters out common words to focus on meaningful content
- **Customizable Summary Length**: Allows users to specify the number of summary sentences
- **Statistics Display**: Shows total word count and sentence count

## Requirements

```bash
pip install PyPDF2
```

## Usage

### Basic Usage

```bash
python pdf_summarizer_and_topic_highlighter.py <pdf_file>
```

### Custom Summary Length

```bash
python pdf_summarizer_and_topic_highlighter.py <pdf_file> <number_of_sentences>
```

### Example

```bash
# Generate a 5-sentence summary (default)
python pdf_summarizer_and_topic_highlighter.py research_paper.pdf

# Generate a 10-sentence summary
python pdf_summarizer_and_topic_highlighter.py research_paper.pdf 10
```

## Output

The tool provides:

1. **Summary**: A concise summary of the PDF content with the most important sentences
2. **Key Topics**: A ranked list of the 15 most frequent topics/keywords with their frequencies
3. **Statistics**: Total word count and sentence count from the PDF

## How It Works

1. **Text Extraction**: Reads the PDF and extracts text from all pages
2. **Text Cleaning**: Normalizes text by removing special characters and extra whitespace
3. **Sentence Splitting**: Breaks text into individual sentences
4. **Word Frequency Analysis**: Calculates word frequencies while filtering stop words
5. **Sentence Scoring**: Scores each sentence based on the importance of words it contains
6. **Summary Generation**: Selects top-scored sentences for the summary
7. **Topic Extraction**: Identifies the most frequent meaningful words as key topics

## Benefits for Students & Researchers

- **Time-Saving**: Quickly understand lengthy documents without reading every page
- **Research Efficiency**: Identify relevant papers by reading summaries first
- **Study Aid**: Extract key concepts and topics for exam preparation
- **Literature Review**: Process multiple papers efficiently
- **Focus on Important Content**: Highlights the most significant information

## Limitations

- Works best with text-based PDFs (may not work well with scanned PDFs)
- Summary quality depends on the structure and content of the PDF
- Currently supports English language content

## Author

Created as part of the 100 Lines of Python Code project.

## License

Feel free to use and modify this tool for your research and study needs!
