import os

# Ask user for folder path
folder_path = input("Enter folder path: ")

# Ask user for prefix
prefix = input("Please enter file name prefix (example: history, img, file): ")

# Check if folder exists
if not os.path.exists(folder_path):
    print("Folder does not exist.")
    exit()

# Get list of files in folder
files = os.listdir(folder_path)

counter = 1

for file in files:
    old_path = os.path.join(folder_path, file)

    # Skip folders
    if os.path.isdir(old_path):
        continue

    # Get file extension
    name, extension = os.path.splitext(file)

    # Create new file name using prefix
    new_name = f"{prefix}_{counter}{extension}"
    new_path = os.path.join(folder_path, new_name)

    # Rename file
    os.rename(old_path, new_path)

    print(f"Renamed: {file} → {new_name}")

    counter += 1

print("Renaming complete.")