def factorial(num: int) -> int:
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)

res = factorial(5)
print(res)