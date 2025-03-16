def length_of_last_word(s: str) -> int:
    s = s.strip()
    words = s.split()
    if not words:
        return 0
    return len(words[-1])

print(length_of_last_word("Learn Python"))
print(length_of_last_word("Coding is Fun"))
print(length_of_last_word("fly me to the moon"))
