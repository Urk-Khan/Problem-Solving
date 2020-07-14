import numpy as np
class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        Prefix_Sum = [0] * len(arr)
        Prefix_Sum[0] = arr[0]
        reverse_map = {}

        for i in range(1, len(arr)):
        	sm = Prefix_Sum[i - 1] + arr[i]
        	Prefix_Sum[i] = sm
        	reverse_map[sm] = i

       	array_present = []

        for i in xrange(len(arr)):
        	if i == 0:
        		if Prefix_Sum[i] == target:
        			array_present.append(True)
				continue
			if Prefix_Sum[i] - target in reverse_map:
				array_present.append(True)
			else:
				array_present.append(False)

		print array_present

arr = [3,2,2,4,3]
target = 3

sol = Solution()
sol.minSumOfLengths(arr, target)