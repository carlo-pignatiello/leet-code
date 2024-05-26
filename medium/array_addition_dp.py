def array_addition(arr: list) -> bool:
    largest = max(arr)
    arr.remove(largest)
    s = sum(arr)
    return False if check_sum(arr, largest - s) else True


def check_sum(arr: list, target: int) -> bool:
    if target == 0:
        return True
    if len(arr) == 0:
        return False
    current = arr[0]
    remainig = arr[1:]
    return check_sum(remainig, target) or check_sum(remainig, target - current)


print(array_addition([5, 7, 16, 1, 2]))
