class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        if len(str) <= 0:
            return 0
        
        for idx, c in enumerate(str):
            if c != ' ':
                break
                
        str = str[idx:]
        
        neg = False
        
        if str[0] == '-':
            neg = True
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
    
        nums = []
        
        for idx, c in enumerate(str):
            if ord(c) < 48 or ord(c) > 57:
                break
            nums.append(ord(c) - 48)
        
        if len(nums) == 0:
            return 0
        
        nums = nums[::-1]
        val = 0
        for idx, num in enumerate(nums):
            val += num * 10 ** idx
        
        if neg:
            val *= -1

        if val < -(2 ** 31):
            val = -(2 ** 31)
        elif val > (2 ** 31 - 1):
            val = 2 ** 31 - 1
        return val

sol = Solution()

print sol.myAtoi("2147483648")