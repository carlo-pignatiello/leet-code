def simple_mode(arr: list) -> int:
    hs = {}
    for i in arr:
        if i not in hs.keys():
            hs[i] = 1
        else:
            c = hs[i] + 1
            hs[i] = c
    if all(x == 1 for x in hs.values()):
        return -1
    return max(hs, key=hs.get)


print(simple_mode([5, 5, 2, 2, 1]))
print(simple_mode([3, 4, 1, 6, 10]))
