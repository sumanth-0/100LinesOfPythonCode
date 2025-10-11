# === Introduction ===
# This code represents a solution to the "12 Days of Christmas" Code Golf challenge.

# If you does not know what Code Golf is, you can read the following article: https://en.wikipedia.org/wiki/Code_golf
#   > Code golf is a type of recreational computer programming competition in which participants strive to
#   > achieve the shortest possible source code that solves a certain problem.

# === Solution ===
# The following code will place you in the top 100 (Bytes & Characters) in October 2025 on the website https://code.golf
# (Please, never write code like this in a real project, this dont accomplish any coding standard).

for e in range(12):print("On the %s day of Christmas\nMy true love sent to me"%"First Second Third Fourth Fifth Sixth Seventh Eighth Ninth Tenth Eleventh Twelfth".split()[e],*"Twelve Drummers Drumm^Eleven Pipers Pip^Ten Lords-a-Leap^Nine Ladies Danc^Eight Maids-a-Milk^Seven Swans-a-Swimm^Six Geese-a-Lay^Five Gold Rings,|Four Calling Birds,|Three French Hens,|Two Turtle Doves, and|A Partridge in a Pear Tree.\n".replace("^","ing,|").split("|")[~e:],sep="\n")

# === Explanation ===
# Here is an uncompressed and explained review of that code.

# We iterate for each day.
for day_number in range(12):
    # Here we create the sentence: "On the [First|Second|...|Twelfth] day of Christmas\nMy true love sent to me"
    day_reference = "First Second Third Fourth Fifth Sixth Seventh Eighth Ninth Tenth Eleventh Twelfth".split()[day_number]
    intro = "On the %s day of Christmas\nMy true love sent to me" % day_reference

    # Here we have a "shorter" version of the following text:
    #
    #   "Twelve Drummers Drumming,|Eleven Pipers Piping,|Ten Lords-a-Leaping,|Nine Ladies Dancing,|Eight Maids-a-Milking,|Seven Swans-a-Swimming,|Six Geese-a-Laying,|Five Gold Rings,|Four Calling Birds,|Three French Hens,|Two Turtle Doves, and|A Partridge in a Pear Tree.\n"
    #
    # We use "^" as a placeholder for "ing" to save characters.
    #
    # Original: 266 characters.
    # Shortened: 260 characters.
    gifts = "Twelve Drummers Drumm^Eleven Pipers Pip^Ten Lords-a-Leap^Nine Ladies Danc^Eight Maids-a-Milk^Seven Swans-a-Swimm^Six Geese-a-Lay^Five Gold Rings,|Four Calling Birds,|Three French Hens,|Two Turtle Doves, and|A Partridge in a Pear Tree.\n".replace("^", "ing,|")

    # We split the string into a list using "|" as the delimiter.
    gifts_list = gifts.split("|")

    # We use "~day_number" to get the negative index equivalent to "len(gifts) - day_number - 1".
    # For example, at day 5, we want to print gifts[7:] (the last 7 gifts).
    # Another example, at day 3, we want to print gifts[9:] (the last 9 gifts).
    gifts_to_print = gifts_list[~day_number:]

    # Then, we just print each gift on a new line with the initial intro.
    print(intro, *gifts_to_print, sep="\n")
