def findGCD(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    mi = min(nums)
    ma = max(nums)
    for i in range(mi, 0, -1):
        if mi % i == 0 and ma % i == 0:
            return i


nums = [7, 5, 6, 8, 3]
print(findGCD(nums))
