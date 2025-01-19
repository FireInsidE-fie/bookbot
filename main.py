def word_count(text):
    count = 0

    for word in text.split():
        count += 1
    return count

def main():
    path = "books/frankenstein.txt"
    total_words = 0

    print("[!] - Beginning execution...")
    print(f"[!] - Printing contents of {path}")

    with open(path) as f:
        for line in f:
            print(line.strip())
            total_words += word_count(line.strip())

    print(f"[?] - Input text contained {total_words} words")

    print("[!] - Exiting...")

main()
