class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        table = []
        
        for idx, c in enumerate(s):
            curr = False
            for j in xrange(idx + 1):
                curr = s[j : idx + 1] in wordDict
                if j > 0:
                    curr = curr and table[j - 1]
                if curr:
                    break 
            table.append(curr)
        return table[-1]

s = "a"
wordDict = ["a"]
sol = Solution()
print sol.wordBreak(s, wordDict)