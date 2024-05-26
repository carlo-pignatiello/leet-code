m = [0 for i in range(1000)]


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    if m[n] != 0:
        return m[n]
    m[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return m[n]


print([fibonacci(n) for n in range(15)])
