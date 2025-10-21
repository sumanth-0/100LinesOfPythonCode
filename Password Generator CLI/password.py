import argparse  # handles command-line arguments
import random    # used to generate random values

# Character pools for password generation
letter_pool = "abcdefghijklmnopqrstuvwxyz"
LETTER_POOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers_pool = "1234567890"
symbols_pool = "!@#$%^&*()-_=+[]{};:,.?/\\|~"
final_pool = ""   # will contain the final set of characters to use
password = ""     # placeholder for generated password

# Create a parser for command-line arguments
parser = argparse.ArgumentParser(description="CLI integrated password generator")

# Define possible arguments
parser.add_argument("--length", type=int, help="length of password", default=10)
parser.add_argument("--n", type=int, help="number of passwords to create", default=1)
parser.add_argument("--symbols", type=int, help="include symbols? 1 for TRUE", default=1)
parser.add_argument("--letters", type=int, help="include letters? 1 for TRUE", default=1)
parser.add_argument("--numbers", type=int, help="include numbers? 1 for TRUE", default=1)

# Parse the arguments from terminal input
args = parser.parse_args()

# Build the final pool based on user choices
if args.symbols == 1:
    final_pool = final_pool + symbols_pool
if args.letters == 1:
    final_pool = final_pool + letter_pool + LETTER_POOL
if args.numbers == 1:
    final_pool = final_pool + numbers_pool

# Generate and print passwords
for i in range(args.n):
    password = ""  # reset password each iteration
    for j in range(args.length):
        password = password + random.choice(final_pool)  # add random character
    print(f"[{i+1}] {password}")  # print generated password with index
