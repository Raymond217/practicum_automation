import os
# Imports the os module, which allows interaction with the operating system
# (used here for file/folder handling like listing files and renaming them)

current_folder = None
# Stores the folder path selected by the user
# Starts as None because no folder is chosen yet

while True:
# Creates an infinite loop so the program keeps running until the user exits

    print("\n=== FILE RENAMER MENU ===")
    # Displays the menu title each time the loop runs

    print("1. Choose folder (enter file path)")
    # Option 1: lets user select a folder

    print("2. Rename (manual trigger)")
    # Option 2: manually trigger renaming (backup option)

    print("3. Exit")
    # Option 3: exit the program

    choice = input("Enter your choice (1, 2, or 3): ")
    # Takes user input for menu selection

    if choice.lower() == "exit" or choice == "3":
    # Checks if user wants to exit (either by typing "exit" or "3")

        print("Exiting program.")
        # Prints exit message

        break
        # Stops the loop and ends the program

    elif choice.lower() == "choose" or choice == "1":
    # Checks if user selected folder option

        folder_path = input("Enter folder path: ")
        # Asks user to input the folder path

        if not os.path.exists(folder_path):
        # Checks if the folder path actually exists

            print("Folder does not exist.")
            # Error message if invalid path

            continue
            # Skips rest of loop and returns to menu

        current_folder = folder_path
        # Saves valid folder path to variable

        print(f"Folder set to: {current_folder}")
        # Confirms folder selection

        prefix = input("Enter file name prefix (example: img, doc, file): ")
        # Asks user for naming prefix for new file names

        files = os.listdir(current_folder)
        # Gets list of all files and folders inside selected directory

        counters = {}
        # Dictionary to track numbering per file extension

        for file in files:
        # Loops through every item in the folder

            old_path = os.path.join(current_folder, file)
            # Creates full path to current file

            if os.path.isdir(old_path):
            # Checks if item is a folder

                continue
                # Skips folders (only renames files)

            name, extension = os.path.splitext(file)
            # Splits file into name and extension (e.g. "cat", ".jpg")

            if extension not in counters:
            # If this file type hasn't been seen before

                counters[extension] = 1
                # Start numbering from 1 for this extension

            count = counters[extension]
            # Gets current number for this extension

            new_name = f"{prefix}_{count}{extension}"
            # Creates new filename using prefix + number + extension

            new_path = os.path.join(current_folder, new_name)
            # Builds full path for renamed file

            os.rename(old_path, new_path)
            # Renames the file on disk

            print(f"Renamed: {file} → {new_name}")
            # Prints what was renamed

            counters[extension] += 1
            # Increases counter for this extension

        print("Renaming complete.")
        # Shows completion message

    elif choice.lower() == "rename" or choice == "2":
    # Manual rename option (same logic as above)

        if current_folder is None:
        # Checks if folder was selected first

            print("No folder selected. Please select a folder first.")
            # Error message

            continue
            # Returns to menu

        prefix = input("Enter file name prefix (example: img, doc, file): ")
        # Asks for prefix again

        files = os.listdir(current_folder)
        # Gets files from selected folder

        counters = {}
        # Resets counters

        for file in files:
        # Loops through files

            old_path = os.path.join(current_folder, file)
            # Full file path

            if os.path.isdir(old_path):
            # Skip folders

                continue

            name, extension = os.path.splitext(file)
            # Split file name

            if extension not in counters:
            # First time seeing this extension

                counters[extension] = 1

            count = counters[extension]
            # Get number

            new_name = f"{prefix}_{count}{extension}"
            # Build new name

            new_path = os.path.join(current_folder, new_name)
            # Build new path

            os.rename(old_path, new_path)
            # Rename file

            print(f"Renamed: {file} → {new_name}")
            # Print result

            counters[extension] += 1
            # Increment counter

        print("Renaming complete.")
        # Done message

    else:
    # If input doesn't match any option

        print("Invalid choice. Please enter 1, 2, or 3.")
        # Error message