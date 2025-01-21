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

def main():
    path = "books/frankenstein.txt"
    total_words = 0

    print("[!] - Beginning execution...")
    print(f"[!] - Printing contents of {path}")

    with open(path) as f:
        characters = character_count(f)
    with open(path) as f: # Should probably find a way to do the word counting at the same time as char counting
        for line in f:
            print(line.strip())
            total_words += word_count(line.strip())

    print(f"[?] - Input text contained {total_words} words")
    print(f"[?] - Now printing dictionary of characters contained...")

    print(characters)

    print("[!] - Exiting...")

main()
