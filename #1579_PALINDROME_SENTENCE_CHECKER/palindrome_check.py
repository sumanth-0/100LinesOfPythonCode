import string
def clean(sentence):
    #Remove spaces and punctuation, and convert to lowercase.
    translator=str.maketrans('','',string.punctuation+' ')
    return sentence.translate(translator).lower()

def is_palindrome(sentence):
    cleaned=clean(sentence)
    return cleaned==cleaned[::-1]

def check(file_path):
    #Read a .txt file and check each line/sentence for palindrome.
    try:
        with open(file_path,'r',encoding='utf-8') as f:
            for line_number, line in enumerate(f,1):
                line=line.strip()
                if not line:
                    continue
                if is_palindrome(line):
                    print(f"Line {line_number} is a palindrome")
                else:
                    print(f"Line {line_number} is NOT a palindrome")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

if __name__ == "__main__":
    check('input_p.txt')
