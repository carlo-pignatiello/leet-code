def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n -2)

print([fibonacci(n) for n in range(15)])
