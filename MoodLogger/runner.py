import csv, os
from datetime import datetime
CSV_FILE='mood_log.csv'
PASS_FILE=os.path.expanduser('~/.mood_pass')
DATE_FORMAT="%Y-%m-%d"

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE,'w',newline='') as f:
            csv.writer(f).writerow(['Date','Mood','Notes'])
import msvcrt

def input_password(prompt="Password: "):
    print(prompt, end='', flush=True)
    pwd = ''
    while True:
        ch = msvcrt.getch()
        if ch in [b'\r', b'\n']:
            print()
            break
        elif ch == b'\x08':  # backspace
            if len(pwd) > 0:
                pwd = pwd[:-1]
                print('\b \b', end='', flush=True)
        else:
            pwd += ch.decode('utf-8')
            print('*', end='', flush=True)
    return pwd


def read_logs():
    if not os.path.exists(CSV_FILE): return []
    with open(CSV_FILE,'r') as f: return list(csv.DictReader(f))

def write_logs(logs):
    with open(CSV_FILE,'w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['Date','Mood','Notes']); w.writeheader(); w.writerows(logs)

def get_log_for_date(logs,date_str):
    for log in logs:
        if log['Date'].startswith(date_str): return log
    return None

def get_password():
    if not os.path.exists(PASS_FILE):
        print("=== FIRST-TIME SETUP ===")
        pwd=input_password("Set a password: ").strip()
        if pwd=='': print("Password cannot be empty. Exiting."); exit()
        with open(PASS_FILE,'w') as f: f.write(pwd)
        return pwd
    with open(PASS_FILE,'r') as f: return f.read()

def input_date(prompt):
    while True:
        d=input(prompt).strip()
        if d=='': return datetime.now().strftime(DATE_FORMAT)
        try: datetime.strptime(d,DATE_FORMAT); return d
        except ValueError: print("Invalid date format. Use YYYY-MM-DD.")

def main():
    print("\n==============================\n      DAILY MOOD LOGGER       \n==============================\n")
    password=get_password()
    if input_password("Enter password: ").strip()!=password:
        print("Wrong password. Access denied.\n If you forgot password, please refer to the Markdown document here."); return
    init_csv(); logs=read_logs()
    print("\nOptions:\n1. Log/update today's mood\n2. Log/update past day\n3. View all history")
    choice=input("\nSelect (1-3): ").strip()
    if choice=='1': date_str=datetime.now().strftime(DATE_FORMAT)
    elif choice=='2': date_str=input_date("Enter date (YYYY-MM-DD, empty=today): ")
    elif choice=='3':
        if not logs: print("\nNo mood records.\n")
        else:
            print("\n--- MOOD HISTORY ---")
            for l in logs: print(f"{l['Date']} | {l['Mood']} | {l['Notes']}")
            print("--------------------\n")
        return
    else: print("Invalid option. Exiting.\n"); return
    existing=get_log_for_date(logs,date_str)
    if existing:
        print(f"\nExisting entry for {date_str}: {existing['Mood']} | {existing['Notes']}")
        if input("Update it? (y/n): ").strip().lower()!='y': return
        logs.remove(existing)
    mood=input("Enter your mood: ").strip()
    notes=input("Optional notes: ").strip()
    logs.append({'Date':date_str+" "+datetime.now().strftime("%H:%M:%S"),'Mood':mood,'Notes':notes})
    write_logs(logs)
    print(f"\nMood saved for {date_str}.\n")
    if input("View all logs? (y/n): ").strip().lower()=='y':
        print("\n--- MOOD HISTORY ---")
        for l in logs: print(f"{l['Date']} | {l['Mood']} | {l['Notes']}")
        print("--------------------\n")

if __name__=='__main__': main()
