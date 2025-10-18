from pathlib import Path

def main():
    dir_path = input("Enter the folder path you want to check: ")
    target_dir = Path(dir_path)

    if not target_dir.exists() or not target_dir.is_dir():
        print("Invalid folder path.")
        return

    file_list = list(target_dir.iterdir())

    observed = set()
    duplicates = []

    for file in file_list:
        if file in observed:
            duplicates.append(file)
        else:
            observed.add(file)

    if duplicates:
        print("Duplicate files found:")
        for file in duplicates:
            print(file)
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main()
