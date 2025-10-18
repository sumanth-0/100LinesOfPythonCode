#  Quick Reminder Script

A simple **Python command-line reminder tool** that waits for a specified amount of time before displaying a reminder message.
Ideal for quick breaks, short tasks, or time-based alerts during work or study sessions.

---

##  Features

*  Set a **custom reminder message**
*  Specify the **delay time (in seconds)**
*  Displays a **reminder notification** after the wait time
*  Uses built-in Python `time` module (no external dependencies)

---

## How It Works

1. The user inputs a reminder message.
2. The user enters the number of seconds to wait.
3. The program pauses using `time.sleep()`.
4. After the delay, it prints the reminder message and a motivational message.

---


---

##  Usage

### **Run the Script**

```bash
python reminder.py
```

### **Example Run**

```
Please tell me what to remind you: Take a break!
Enter wait time in seconds (e.g., 5): 5
⏰ Reminder set for 'Take a break!'. Waiting for 5 seconds...

*********************************
🚨 REMINDER: Take a break!
*********************************

Hey get back to your reminded work !!!
```

---

##  Notes

* The script **blocks execution** during the wait (no multitasking).
* To make it **non-blocking**, you could use threading or async techniques.
* Works on any OS with Python 3 installed.

---

##  Requirements

* Python 3.x
* No additional libraries required.

---
