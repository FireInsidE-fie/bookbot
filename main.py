def word_count(text):
    count = 0

    for word in text.split():
        count += 1
    return count

def character_count(text):
    characters = {}
    for line in text:
        for char in line:
            char = char.lower()
            if char in characters:
                characters[char.lower()] += 1
            else:
                characters[char] = 1
    return characters

def print_report(path, characters, total_words):
    print(f"[!] - Beginning report for {path}...")
    print(f"[!] - Total words: {total_words}")
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
