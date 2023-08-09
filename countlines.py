import os
import re
import tkinter as tk
from tkinter import filedialog

def count_lines_and_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        line_count = len(lines)

        # Count words by splitting on whitespace characters
        word_count = sum(len(re.findall(r'\w+', line)) for line in lines)

    return line_count, word_count

def count_code_in_folder(folder_path):
    total_lines = 0
    total_words = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                lines, words = count_lines_and_words(file_path)
                total_lines += lines
                total_words += words

    return total_lines, total_words

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    folder_path = filedialog.askdirectory(title="Select Folder")

    if folder_path:
        total_lines, total_words = count_code_in_folder(folder_path)
        print(f"Total lines of code: {total_lines}")
        print(f"Total words of code: {total_words}")
    else:
        print("No folder selected.")

if __name__ == "__main__":
    select_folder()
