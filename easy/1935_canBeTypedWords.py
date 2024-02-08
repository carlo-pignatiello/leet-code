# Exercise 1935

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        # bit faster version
        counter = len(text.split(" "))
        text_splitted = text.split(" ")
        for i in text_splitted:
            if len(set(brokenLetters).intersection(set(list(i)))):
                counter -= 1
        return counter
        
        # slow version
        
        # counter = len(text_splitted)
        # for i in text_splitted:
        #     for j in brokenLetters:
        #         if j in i:
        #             counter -= 1
        #             break
        # return counter
                    
if __name__ == "__main__":
    # text = "hello world"
    # brokenLetters = "ad"
    text = "leet code"
    brokenLetters = "lt"
    # text = "leet code"
    # brokenLetters = "e"
    s = Solution()
    h = s.canBeTypedWords(text, brokenLetters)
    print(h)