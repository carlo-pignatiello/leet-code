def compress_string(s: str) -> str:
    compressed = ""
    counter_letter = 0
    for idx, letter in enumerate(s):
        counter_letter += 1
        if idx + 1 >= len(s) or letter != s[idx + 1]: 
            compressed = compressed + str(counter_letter) + letter
            counter_letter = 0
    return compressed

res = compress_string("hhhiic")
print(res)