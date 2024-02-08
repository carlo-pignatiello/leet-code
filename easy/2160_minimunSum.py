# Exercise 2160

class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_splitted = list(str(num))
        num = []
        while len(num_splitted):
            m = max(num_splitted)
            num.append(m)
            num_splitted.remove(m)
        return int(num[3] + num[0]) + int(num[2] + num[1])


if __name__ == "__main__":
    num = 2932
    s = Solution()
    h = s.minimumSum(num=num)
    print(h)
