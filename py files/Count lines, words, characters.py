import os

def count(file_path):

    lines = 0
    words = 0
    characters = 0

    with open(file_path, "r") as f:
        for line in f:
            lines += 1
            words += len(line.split())
            characters += len(line)

    return lines, words, characters


file_path = input("Enter the path to the file: ")

lines, words, characters = count(file_path)

print("Lines:", lines)
print("Words:", words)
print("Characters:", characters)