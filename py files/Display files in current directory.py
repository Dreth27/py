import os

def display_files_in_current_directory():

    files = os.listdir()

    print("Files in the current directory:")
    for file in files:
        print(file)


display_files_in_current_directory()