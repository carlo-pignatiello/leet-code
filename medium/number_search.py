import math


def number_search(s: str) -> int:
    counter_letter = 0
    counter_number = 0
    for i in s:
        if i.isdigit():
            counter_number += int(i)
        else:
            counter_letter += 1

    return math.ceil(counter_number / counter_letter)


res = number_search("h3ello9-9")
print(res)
