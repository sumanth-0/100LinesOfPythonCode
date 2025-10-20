import re
import random

MADLIBS = [
    """It was about <number> <measure_of_time> ago when I came to the hospital in a <mode_of_transportation>.
The hospital is a/an <adjective> place, there are a lot of <adjective> <noun> here.
There are nurses here who have <color> <part_of_body>.
If someone wants to come into my room I told them that they have to <verb> first.
I have decorated my room with <number> <noun>.
Today a doctor came into my room and they were wearing a <noun> on their <part_of_body>.
I heard that all doctors <verb> <noun> every day for breakfast.
The most <adjective> thing about being in the hospital is the <noun> <silly_word>!""",

    """Dear <person_name>,
I am writing to you from a <adjective> castle in an enchanted forest. I found myself here one day after going for a ride on a <color> <animal> in <place>.
There are <adjective> <magical_creature_plural> and <adjective> <magical_creature_plural> here!
In the <room_in_house> there is a pool full of <noun>.
I fall asleep each night on a <noun> of <noun> and dream of <noun> <noun>.
It feels as though I have lived here for <number> <measure_of_time>.
I hope one day you can visit, although the only way to get here now is <verb_ing> on a <adjective> <noun>!!""",

    """All of my <noun> I wanted a <animal> to <verb> with in the <place>.
A <animal> would be so <adjective>, soft, and cuddly.
We would <verb> together every afternoon and she would <verb> next to my <noun> at night.
My <person> says I can’t have a <animal> until I learn to <verb> my <place> and take out the <noun>.
I hate <verb_ing>, but I’ll do it if I can have a <adjective> <animal> to <verb> with!""",

    """The <adjective> <noun> jumped over the <adjective> <noun> and ran to the <place>.
Suddenly, the <noun> started to <verb> loudly, causing everyone to turn their <part_of_body> in surprise.
At that moment, a <adjective> <noun> appeared and offered a <noun> filled with <plural_noun>.
Everyone shouted '<exclamation>!' and danced around the <place> until <number> o'clock.""",

    """Last summer, my family went to <place> for vacation.
On the first day, we saw a <adjective> <animal> that tried to <verb> my sandwich.
Later, we rented a <mode_of_transportation> and rode to a <adjective> <noun> where we swam with <plural_noun>.
My favorite part was when Dad slipped on a <noun> and everyone laughed so hard, their <part_of_body> hurt.
By the end of the trip, we decided to <verb> back every year!"""
]

def mad_lib_generator():

    # Welcome the user.
    print("Welcome to the.... MADlibs Generatorrrrrr! A random story will be chosen for you, hang on!")

    # Select a story.
    madlib = random.choice(MADLIBS)

    # Find placeholders.
    matches = re.findall(r"<(.*?)>", madlib)

    # Get user input.
    answers = []
    for match in matches:
        answers.append(input(f"Enter a {match}: "))

    # Helper function to substitute sequentially.
    def replacer(match):
        return answers.pop(0)

    # Substitute and print the result
    result = re.sub(r"<(.*?)>", replacer, madlib)
    print(result)

mad_lib_generator()