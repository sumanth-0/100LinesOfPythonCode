import datetime

def log_gratitude(entries):
    print("\nToday's gratitude entries:")
    for idx, entry in enumerate(entries, 1):
        print(f"{idx}. {entry}")
    if not entries:
        print("No entries logged.")

def save_log(entries):
    date = datetime.date.today()
    fname = f"gratitude_{date}.txt"
    with open(fname, "w") as f:
        for idx, entry in enumerate(entries, 1):
            f.write(f"{idx}. {entry}\n")
    print(f"Entries saved to {fname}")

def logger():
    print("Welcome to Gratitude Logger")
    entries = []
    while True:
        entry = input("Enter something you're grateful for (leave blank to finish): ").strip()
        if not entry:
            break
        entries.append(entry)
    log_gratitude(entries)
    if entries:
        save = input("Save entries to file? (y/n): ").strip().lower()
        if save == 'y':
            save_log(entries)

def main():
    logger()

if __name__ == "__main__":
    main()
