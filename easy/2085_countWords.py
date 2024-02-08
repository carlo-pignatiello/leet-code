class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        w_1 = self.remove_double(words1)
        w_2 = self.remove_double(words2)
        return len(w_1.intersection(w_2))

    def remove_double(self, num) -> set:
        d = {}
        for i in num:
            if i in d.keys():
                d[i] = -1
            else:
                d[i] = 0
        d = {k:v for k, v in d.items() if v == 0}
        return set(d.keys())


if __name__ == "__main__":
    words1 = ["leetcode", "is", "amazing", "as", "is"]
    words2 = [
        "amazing",
        "leetcode",
        "is",
    ]
    # words1 = ["b", "bb", "bbb"]
    # words2 = ["a", "aa", "aaa"]
    # words1 = ["a","ab"]
    # words2 = ["a","a","a","ab"]
    s = Solution()
    h = s.countWords(words1, words2)
    print(h)
