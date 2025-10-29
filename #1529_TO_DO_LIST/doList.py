import json, os, sys
from datetime import datetime

DATA = "tasks.json"

def load(): return json.load(open(DATA)) if os.path.exists(DATA) else []
def save(t): json.dump(t, open(DATA, "w"), indent=2)
def parse_dt(s):
    for f in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try: return datetime.strptime(s.strip(), f)
        except: pass
    return None

def add_task(t):
    title = input("enter the title: ").strip()
    if not title: return print("Empty title; cancelled.")
    dt = parse_dt(input("Due (YYYY-MM-DD or YYYY-MM-DD HH:MM): "))
    if not dt: return print("Invalid date format; cancelled.")
    t.append({"title": title, "due": dt.isoformat(), "done": False})
    save(t); print("Added.")

def list_tasks(t):
    if not t: return print("No tasks.")
    for i,x in enumerate(sorted(t, key=lambda k:k["due"]),1):
        d = datetime.fromisoformat(x["due"])
        s = "✓" if x["done"] else " "
        print(f"{i}. [{s}] {x['title']} — {d:%Y-%m-%d %H:%M}")

def mark_done(t):
    list_tasks(t)
    if not t: return
    try: n=int(input("Mark task #: "))
    except: return print("Invalid number.")
    s=sorted(t,key=lambda k:k["due"])
    if 1<=n<=len(s):
        sel=s[n-1]
        for x in t:
            if x["title"]==sel["title"] and x["due"]==sel["due"]: x["done"]=True
        save(t); print("Marked done.")
    else: print("Out of range.")

def delete_task(t):
    list_tasks(t)
    if not t: return
    try:n=int(input("Delete task #: "))
    except:return print("Invalid number.")
    s=sorted(t,key=lambda k:k["due"])
    if 1<=n<=len(s):
        sel=s[n-1]; t[:]=[x for x in t if not(x["title"]==sel["title"] and x["due"]==sel["due"])]
        save(t); print("Deleted.")
    else: print("Out of range.")

def next_due(t):
    now=datetime.now()
    up=[(x,datetime.fromisoformat(x["due"])) for x in t if not x["done"]]
    if not up: return print("No upcoming tasks.")
    up.sort(key=lambda p:p[1]); x,d=next(((a,b) for a,b in up if b>=now),up[0])
    dt=d-now; days,hrs,mins=dt.days,dt.seconds//3600,(dt.seconds%3600)//60
    when=f"in {days}d {hrs}h {mins}m" if dt.total_seconds()>=0 else "overdue"
    print(f"Next: {x['title']} — {d:%Y-%m-%d %H:%M} ({when})")

def menu():
    t=load()
    opts={"1":("Add",add_task),"2":("List",list_tasks),"3":("Next",next_due),
          "4":("Mark done",mark_done),"5":("Delete",delete_task),"q":("Quit",lambda _:sys.exit())}
    while True:
        print("\nTo-Do Notifier")
        [print(f"{k}) {v[0]}") for k,v in opts.items()]
        c=opts.get(input("Choose: ").strip())
        c[1](t) if c else print("Invalid choice.")

if __name__=="__main__": menu()
