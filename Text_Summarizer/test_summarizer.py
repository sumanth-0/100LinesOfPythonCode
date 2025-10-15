"""Test script for text_summarizer.py"""
import sys
sys.path.append('.')
from text_summarizer import extract_top_sentences
# test_summarizer.py
# Test with a sample paragraph
test_text = """
Artificial intelligence is transforming the world. Machine learning algorithms can now
recognize patterns in vast amounts of data. Deep learning, a subset of machine learning,
uses neural networks with multiple layers. These technologies are being applied in healthcare,
finance, and many other fields. AI systems can diagnose diseases, predict market trends,
and even drive cars autonomously. The future of AI looks promising with continuous advancements.
"""

print("Testing Text Summarizer...")
print("=" * 60)
print("\nOriginal Text:")
print(test_text)

print("\n" + "=" * 60)
print("Extracting top 3 sentences...")
print("=" * 60)

top_sentences = extract_top_sentences(test_text, num_sentences=3)

for i, sentence in enumerate(top_sentences, 1):
    print(f"\n{i}. {sentence}")

print("\n" + "=" * 60)
print("Test completed successfully!")
