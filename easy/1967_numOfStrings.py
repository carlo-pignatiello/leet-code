class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        counter = len(patterns)
        for i in patterns:
            if i not in word:
                counter -= 1
        return counter


if __name__ == "__main__":
    patterns = ["a", "abc", "bc", "d"]
    word = "abc"
    patterns = ["a", "b", "c"]
    word = "aaaaabbbbb"
    s = Solution()
    h = s.numOfStrings(patterns, word)
    print(h)
