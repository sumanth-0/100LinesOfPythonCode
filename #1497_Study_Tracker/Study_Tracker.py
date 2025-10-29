import json, os
from datetime import date

FILE = "study_log.json"
def load_data():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return []
def save_data(data):
    with open(FILE,"w") as f: json.dump(data,f,indent=2)
def add_entry():
    data = load_data()
    subj = input("Enter the subject: ").title()
    hrs = float(input("Enter the hours studied for the subject: "))
    data.append({"date":date.today().isoformat(),"subject":subj,"hours":hrs})
    save_data(data)
    print("Your entry is added!")

def show_data():
    data = load_data()
    if not data: print("Sorry!!no data is found."); return
    print("\nIndex | Date | Subject | Hours")
    for i,e in enumerate(data):
        print(f"{i:5d} | {e['date']} | {e['subject']} | {e['hours']}")

def edit_entry():
    data = load_data(); show_data()
    if not data: return
    i = int(input("Enter the index to edit: "))
    if 0 <= i < len(data):
        data[i]["subject"] = input("New subjects are: ").title()
        data[i]["hours"] = float(input("New hours updated are: "))
        save_data(data); print("Updated!")
    else: print("Invalid index.")

def delete_entry():
    data = load_data(); show_data()
    if not data: return
    i = int(input("Enter the index to delete: "))
    if 0 <= i < len(data):
        data.pop(i); save_data(data); print("Deleted!")
    else: print("Invalid index.")

def summary():
    data = load_data()
    if not data: print("No data to summarize it."); return
    totals = {}
    for e in data:
        totals[e["subject"]] = totals.get(e["subject"],0)+e["hours"]
    print("\nTotal Hours per Subject:")
    for s,h in totals.items():
        print(f"  {s}: {h} hrs")

def main():
    while True:
        print("\n1.Add  \n2.View  \n3.Edit  \n4.Delete  \n5.Summary  \n6.Exit")
        ch = input("Enter your Choice: ")
        if ch=="1": add_entry()
        elif ch=="2": show_data()
        elif ch=="3": edit_entry()
        elif ch=="4": delete_entry()
        elif ch=="5": summary()
        elif ch=="6": break
        else: print("this is an invalid choice.")

if __name__=="__main__": main()
