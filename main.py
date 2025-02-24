from stats import *

def print_report(path, characters, total_words):
    print(f"[!] - Beginning report for {path}...")
    print(f"[!] - {total_words} words found in the document")
    for char in characters:
        if char.isalpha():
            print(f"Number of '{char}' in text: {characters[char]}")

def main():
    path = "books/frankenstein.txt"
    total_words = 0

    print("[!] - Beginning execution...")
    # print(f"[!] - Printing contents of {path}")

    with open(path) as f:
        characters = character_count(f)
    with open(path) as f: # Should probably find a way to do the word counting at the same time as char counting
        for line in f:
            # print(line.strip())
            total_words += word_count(line.strip())

    print_report(path, characters, total_words)

    print("[!] - Exiting...")

main()
