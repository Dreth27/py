def open_file(file_path):

    try:
        file = open(file_path, "r")
    except FileNotFoundError:
        print("File not found:", file_path)
        return None
    except IOError as e:
        print("Error opening file:", file_path, e)
        return None
    else:
        return file

file_path = input("Enter the file path: ")
file = open_file(file_path)
if file is not None:
    file_contents = file.read()
    print(file_contents)
    file.close()
else:
    print("Could not open file")