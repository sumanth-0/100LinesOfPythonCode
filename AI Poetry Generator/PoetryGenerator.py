import random
from transformers import pipeline


def generate_poem_stanza(model, prompt, num_lines=4):
    generated = model(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
    poem_lines = generated.split('\n')
    return '\n'.join(poem_lines[:num_lines])


def generate_full_poem(model, prompts, num_stanzas=3, lines_per_stanza=4):
    poem = []
    for i in range(num_stanzas):
        prompt = random.choice(prompts)
        stanza = generate_poem_stanza(model, prompt, lines_per_stanza)
        poem.append(stanza)
    return '\n\n'.join(poem)


def print_poem(poem):
    print("=== Your AI-Generated Poem ===\n")
    print(poem)
    print("\n=== End of Poem ===")


def get_user_input():
    try:
        num_stanzas = int(input("Enter the number of stanzas for the poem: "))
        lines_per_stanza = int(input("Enter the number of lines per stanza: "))
    except ValueError:
        print("Invalid input. Using default values.")
        num_stanzas = 3
        lines_per_stanza = 4
    return num_stanzas, lines_per_stanza


def main():
    poetry_generator = pipeline("text-generation", model="gpt2")

    prompts = [
        "In a garden full of dreams,",
        "Under the starry sky of night,",
        "Waves crashing against the shore,",
        "Whispers of the wind in trees,",
        "A moonlit path through the forest,",
        "The sound of rain on silent streets,"
    ]

    num_stanzas, lines_per_stanza = get_user_input()

    poem = generate_full_poem(poetry_generator, prompts, num_stanzas, lines_per_stanza)

    print_poem(poem)


if __name__ == "__main__":
    main()
