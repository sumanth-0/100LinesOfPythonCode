import emoji
from tkinter import Tk
from tkinter.filedialog import askopenfilename

root = Tk() #this instantiates the tikinter window
root.withdraw()# hides the default window
root.attributes('-topmost', True)#this ensures that only default window gets closed and the file window works as expected

#this function launches a tkinter Gui for file selection
def txt_or_log():
    file_path = askopenfilename(title="Select a file")
    if not file_path:
        return (False, "No file selected")
    if any(file_path.endswith(ext) for ext in [".txt", ".log"]):#enusers that the correct file type is uploaded (.txt or .log)
        with open(file_path, "r") as f:
            return (True, f.read())
    else:
        print("Error: Incorrect file type. Allowed types are .txt, .log")
        return (False, "error")

print("\t--\tEmoji Counter\t--\t")
flag = True
while flag:
    print("File Format")
    print("1. Text File(.txt) or Log File(.log)\n2. Paste Text\n3. Exit\n")
    choice = input("Enter Your Choice: ").strip()
    
    emoji_count = 0 #to maintian the count of the emojis

    if choice not in ["1", "2", "3"]:
        print('Invalid choice. Please enter a valid choice 1 to 3\n')
        continue
    elif choice == '3':
        break
    elif choice == '1':
        content_obj = txt_or_log()
        if not content_obj[0]:
            continue
        content = content_obj[1]
    else:
        content = input("Paste the text here:\n")
    #CORE LOGIC
    for c in content: 
        if c in emoji.EMOJI_DATA:#the emoji library consists of all the emojis preserved in an unicode format and provides abstraction to check the emojis
            emoji_count += 1

    print(f"\nThe Number Of Emojis In The Provided Data Is {emoji_count}\n")
