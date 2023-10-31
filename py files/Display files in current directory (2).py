import os

def display_files_in_directory():

    directory_path = input("Enter the directory path: ")

    if not os.path.exists(directory_path):
        print("The directory path does not exist.")
        return

    files = os.listdir(directory_path)

    print("Files in the directory:", directory_path)
    for file in files:
        print(file)


display_files_in_directory()