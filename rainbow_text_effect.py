import time
import sys
colors = ["\033[91m","\033[93m","\033[92m","\033[96m","\033[94m","\033[95m"]
reset = "\033[0m"

text "Hactoberfest 2025"

for letter in text:
  color=colors[hash(letter)%len(colors)]
  sys.stdout.write(color+letter+reset)
  sys.stdout.flush()
  time.sleep(0.1)

print("\n🎉 Enjoy the colors!")
