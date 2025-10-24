import hashlib

def calculate_hash(file):
    hash_sha256 = hashlib.sha256()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def main():
    import os
    import sys

    if len(sys.argv) != 2:
        print("Usage: python file_duplicates_remover.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print(f"The path {directory_path} is not a valid directory.")
        sys.exit(1)

    hashes = {}
    duplicates = []

    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)

            if file_hash in hashes:
                duplicates.append(file_path)
            else:
                hashes[file_hash] = file_path

    for duplicate in duplicates:
        os.remove(duplicate)
        print(f"Removed duplicate file: {duplicate}")

if __name__ == "__main__":
    main()