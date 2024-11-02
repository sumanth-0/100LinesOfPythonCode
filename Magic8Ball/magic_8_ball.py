# magic_8_ball.py
import random

def magic_8_ball():
  """Simulates a Magic 8-Ball."""

  questions = ["Will I win the lottery?", "Should I quit my job?", "Is love in the air for me?"]

  question = input("Ask your question: ")

  answers = [
      "It is certain.",
      "It is decidedly so.",
      "Without a doubt.",
      "Yes - definitely.",
      "You may rely on it.",
      "As I see it, yes.",
      "Most likely.",
      "Outlook good.",
      "Yes.",
      "Signs point to yes.",
      "Reply hazy, try again.",
      "Ask again later.",
      "Better not tell you now.",
      "Cannot predict now.",
      "Concentrate and ask again.",
      "Don't count on it.",
      "My reply is no.",
      "My sources say no.",
      "Outlook not so good.",
      "Very doubtful."
  ]

  random_answer = random.choice(answers)
  print(f"Magic 8-Ball says: {random_answer}")

if __name__ == "__main__":
  magic_8_ball()
