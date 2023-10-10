#regex search
import os
import re

# Function to search for a regular expression in a file
def search_in_file(file_path, regex_pattern):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if re.search(regex_pattern, line):
                print(f"Match found in {file_path}, Line {line_number}: {line.strip()}")

# Function to search for the regular expression in all .txt files in a folder
def search_in_folder(folder_path, regex_pattern):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)
                search_in_file(file_path, regex_pattern)

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    regex_pattern = input("Enter the regular expression to search for: ")
    search_in_folder(folder_path, regex_pattern)
