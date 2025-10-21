import random

# Lists of components for generating prompts
characters = [
    "A jaded detective who can communicate with ghosts",
    "An ambitious street artist with the ability to bring graffiti to life",
    "A retired pirate captain cursed to relive his final storm",
    "A brilliant but socially awkward librarian who hoards forbidden knowledge",
    "A young chef with synesthesia that lets her taste emotions",
    "An immortal watchmaker who repairs time itself",
    "A nomadic hacker collective's charismatic leader",
    "A shape-shifting fox spirit disguised as a folk musician",
    "A bioengineered gardener who grows hybrid plants with personalities",
    "A time-displaced Viking warrior with a poet's soul",
    "A rogue AI therapist specializing in digital dreams",
    "A forgotten folklore scholar who summons mythical beasts",
    "A quantum physicist trapped in parallel realities",
    "A street magician whose illusions bend reality",
    "An eco-warrior with the power to commune with ancient forests"
]

settings = [
    "a derelict Victorian asylum",
    "the neon-lit underbelly of a cyberpunk megacity",
    "a tropical island paradise turned toxic by an ancient volcanic curse",
    "a hidden library beneath the Eiffel Tower during a rare Paris blackout",
    "the frozen wilds of Antarctica",
    "a clockwork steampunk village frozen in 1892",
    "a floating casino in the skies above the Sahara",
    "a remote Appalachian music festival",
    "a rooftop farm in a dystopian flooded Venice",
    "a bustling Tokyo subway during cherry blossom season",
    "a derelict space station orbiting a dying star",
    "an enchanted underwater city of merfolk rebels",
    "a post-apocalyptic desert caravan route",
    "a Victorian-era hot air balloon expedition",
    "a virtual reality coliseum where gladiators fight with code"
]

conflicts = [
    "must solve a haunting, but the spirits demand he sacrifice his own memories to uncover the truth behind their deaths",
    "discovers her murals are escaping, sparking a rebellion against the corporate overlords who control the walls",
    "forcing him to ally with rival smugglers to break the cycle before it consumes the entire archipelago",
    "where the books begin whispering secrets that could rewrite history—but at the cost of her sanity",
    "only to realize her dishes are amplifying the crew's buried resentments, threatening to fracture the isolated research station",
    "tasked with mending a shattered hourglass that holds the villagers' aging souls, but fixing it means erasing his own forgotten past",
    "where the house always wins by manipulating dreams—until she uncovers that the casino's AI is her long-lost sibling, programmed to trap souls for eternity",
    "but her melodies start unraveling the attendees' family curses, drawing vengeful mountain witches who want to silence her forever",
    "where her creations are evolving sentience and demanding rights—pitting her against the city's ruthless water barons who see them as weeds",
    "compelled by an ancient rune to assassinate a modern salaryman whose bloodline erased his clan's legacy from history",
    "who must navigate a patient's subconscious labyrinth to prevent a global empathy collapse",
    "but the beasts she calls forth begin merging with modern technology, creating uncontrollable hybrids",
    "struggling to return home while her choices ripple across infinite timelines",
    "whose tricks start erasing the boundaries between stage and street, attracting the attention of skeptical authorities",
    "battling corporate polluters who seek to silence the trees' prophetic warnings"
]

def generate_prompt():
    char = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    # Simple template to combine
    prompt = f"{char} {setting}, {conflict}"
    return prompt

def main():
    print("Random Story Prompt Generator")
    try:
        num_prompts = int(input("How many prompts? (default 5): ").strip() or "5")
    except ValueError:
        num_prompts = 5
    
    print("\nGenerated Prompts:\n")
    for i in range(num_prompts):
        prompt = generate_prompt()
        print(f"{i+1}. {prompt}")
        print()

if __name__ == "__main__":
    main()
