import unittest

def wordCount(text): 
    text = text.lower()
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    # frequency_keys = sorted(frequency.keys())
    # frequency_sorted = dict(sorted(frequency.items()))
    # frequency_sorted = dict(frequency.items(), reverse=True)
    sorted_items_desc = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    sorted_items_desc = sorted_items_desc[:10]

    mystring = ""
    
    # Iterate over the sorted list of (key, value) tuples
    for i, (key, value) in enumerate(sorted_items_desc):
        # Format the line, using (i+1) for 1-based indexing, 
        # and adding the newline character at the end.
        mystring = mystring + f"{i+1}. {key}: {value}\n"
        
    # rstrip() removes the trailing newline from the last iteration
    return mystring.rstrip()

class TestWordCounter(unittest.TestCase):
    def test_sample_text(self):
        self.assertEqual(wordCount("Dog lion tiger RhiNo CaT horse tiGer dog cAt cat CoW froG cat DOg hUmaN GOrilla rhiNo"), 
                         "{'cat': 4, 'cow': 1, 'dog': 3, 'frog': 1, 'gorilla': 1, 'horse': 1, 'human': 1, 'lion': 1, 'rhino': 2, 'tiger': 2}",
                         msg="Negative - possible problems: not in alphabetical order, incorrect counts, failed case sensitivity")


def main():
    # 1. Define the input text
    sample_text = "Dog lion tiger RhiNo  CaT horse  RaBBit tiGer  dog cAt cat CoW froG cat  DOg hUmaN GOrilla rhiNo  MonkEy"
    print("\n*There are more than 10 unique words")
    print(f"--- Analyzing Text: '{sample_text}' ---")
    # 2. Call the function
    result = wordCount(sample_text)
    # 3. Print a final summary (optional, since wordCount already prints)
    print("\nWord Frequencies (From greatest to least):")
    print(result)

    print("===================================================\n")

    sample_text2 = "Dog lion tiger  RhiNo CaT horse tiGer dog cAt cat  froG cat DOg rhiNo"
    print("*This time there are less than 10 unique words")
    print(f"--- Analyzing Text: '{sample_text2}' ---")
    # 2. Call the function
    result2 = wordCount(sample_text2)
    # 3. Print a final summary (optional, since wordCount already prints)
    print("\nWord Frequencies (from greatest to least):")
    print(result2)

if __name__ == '__main__':
    main() # This line executes the demonstration logic