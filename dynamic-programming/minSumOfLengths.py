import numpy as np
from sys import maxint

def my_print(s, arr):
    print s,
    for val in arr:
        if val == maxint:
            print -1,
        else:
            print val,
    print

class Solution(object):
    def getMinUpTo(self, arr, target):
        Prefix_Sum = [0] * len(arr)
        Prefix_Sum[0] = arr[0]
        reverse_map = {}
        reverse_map[arr[0]] = 0
        for i in range(1, len(arr)):
            sm = Prefix_Sum[i - 1] + arr[i]
            Prefix_Sum[i] = sm
            reverse_map[sm] = i

        min_up_to = []
        reverse_map[0] = -1
        for i in xrange(len(arr)):
            diff = (Prefix_Sum[i] - target)
            if diff in reverse_map and reverse_map[diff] < i:
                min_up_to.append(1 if i == 0 else min(min_up_to[-1], i - reverse_map[diff]))
            else:
                min_up_to.append(maxint if i == 0 else min_up_to[-1])
        return min_up_to

    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        min_up_to = self.getMinUpTo(arr, target)
        arr.reverse()
        min_from = self.getMinUpTo(arr, target)
        min_from.reverse()
        minimum_val = maxint
        for i in xrange(len(min_up_to) - 1):
            val = min_up_to[i] + min_from[i + 1]
            if minimum_val > val:
                print minimum_val, val, i, min_up_to[i], min_from[i + 1]
            minimum_val = min(val, minimum_val)
        return minimum_val if minimum_val != maxint else -1

arr = [3,2,2,4,3]
target = 3
# arr = [7,3,4,7]
# target = 7
# arr = [2,2,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# target = 20

sol = Solution()
print sol.minSumOfLengths(arr, target)