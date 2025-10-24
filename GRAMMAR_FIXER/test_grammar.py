from grammar_fixer import fix_grammar

test_cases = [
    {
        "input": "hello world",
        "expected_output": "Hello world."
    },
    {
        "input": "i love coding it makes me happy do you like python",
        "expected_output": "I love coding. It makes me happy. Do you like python?"
    },
    {
        "input": "this is a sentence. this is another one",
        "expected_output": "This is a sentence. This is another one."
    },
    {
        "input": "what is your name how are you",
        "expected_output": "What is your name? How are you?"
    },
    {
        "input": "   spaces   before and after   ",
        "expected_output": "Spaces before and after."
    },
    {
        "input": "already correct. nothing to fix!",
        "expected_output": "Already correct. Nothing to fix!"
    },
    {
        "input": "MIXED case words here. another SENTENCE",
        "expected_output": "Mixed case words here. Another sentence."
    },
    {
        "input": "multiple    spaces between words",
        "expected_output": "Multiple spaces between words."
    },
    {
        "input": "one-word",
        "expected_output": "One-word."
    },
    {
        "input": "",
        "expected_output": ""
    }
]

for i, test in enumerate(test_cases):
    result = fix_grammar(test["input"])
    if result == test["expected_output"]:
        print(f"Test {i+1}: PASS")
        print(f"  Input: {repr(test['input'])}")
        print(f"  Output: {repr(result)}")
    else:
        print(f"Test {i+1}: FAIL")
        print(f"  Input: {repr(test['input'])}")
        print(f"  Expected: {repr(test['expected_output'])}")
        print(f"  Got: {repr(result)}")