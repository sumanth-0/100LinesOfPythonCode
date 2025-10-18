import datetime
now = datetime.datetime.now()
now=str(now)
print("Welcome to your Gratitude Logger")
print("Hope you had a great day")
z=""
while True:
    #when ever user enters Done logger the code will terminate 
    current_line = input("> ")
    if current_line=="Done Logger":
        break
    else:
        z=z+current_line
z=now+"\n"+z
with open("Gratitude_logger.txt","w") as f:
    f.write(z)