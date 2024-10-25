import random

def get_random_fact():
    facts = [
        "Python is named after the comedy television show 'Monty Python's Flying Circus'.",
        "Java was originally called Oak after an oak tree that stood outside James Gosling's office.",
        "JavaScript was created in just 10 days by Brendan Eich in 1995.",
        "C++ was developed by Bjarne Stroustrup in 1979 at Bell Labs as an extension of the C programming language.",
        "Ruby was created by Yukihiro Matsumoto in the mid-1990s with the intention of making programming fun.",
        "Swift was introduced by Apple in 2014 to replace Objective-C and make iOS development easier.",
        "PHP originally stood for 'Personal Home Page', but it now stands for 'PHP: Hypertext Preprocessor'.",
        "Ada Lovelace is considered the first computer programmer for her work on Charles Babbage's early mechanical general-purpose computer.",
        "The first high-level programming language was Fortran, developed in the 1950s for scientific and engineering applications.",
        "Perl was created by Larry Wall in 1987 and is known for its text-processing capabilities."
    ]
    return random.choice(facts)

def main():
    print("Random Programming Language Fact:")
    print(get_random_fact())

if __name__ == "__main__":
    main()
