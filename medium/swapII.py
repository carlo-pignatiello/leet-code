def swap(s: str) -> str:
    d = {}
    new_s = ""
    for idx, i in enumerate(s):
        if not i.isnumeric():
            new_s = new_s + i
        else:
            d[i] = idx
    if not len(d) % 2 == 0:
        d.popitem()
    for k, v in d.items():
        new_s = new_s[:v] + k + new_s[v:]
    return new_s


print(swap("Hello -5LOL6"))
print(swap("1el2o -5L3L6"))
