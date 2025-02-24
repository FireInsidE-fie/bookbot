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
