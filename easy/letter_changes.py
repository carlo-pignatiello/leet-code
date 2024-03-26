def letter_changes(s: str) -> str:
    new_s = ""
    for i in s:
        next_char = chr(ord(i) + 1)
        if i.isnumeric():
            new_s = new_s + i
        elif next_char in ["a", "e", "i", "o", "u"]:
            new_s = new_s + next_char.capitalize()
        else:
            new_s = new_s + next_char
    return new_s


print(letter_changes("hello*3"))
