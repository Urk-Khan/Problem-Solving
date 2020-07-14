class Solution(object):
    
    def getMedian(self, nums):
    	ln = len(nums)
    	if ln == 0:
    		return -1, -1, -1
    	if ln % 2 == 0: # even
    		l = ln/2 - 1
    		u = ln/2
    		return (nums[u] + nums[l])/2.0, l, u
    	else:
    		l = ln/2
    		u = ln/2
    		return (nums[u] + nums[l])/2.0, l, u

    def merge(self, nums1, nums2):
    	if len(nums1) == 0:
    		return nums2
    	if len(nums2) == 0:
    		return nums1

    	if len(nums1) == 2:
    		if nums2[0] < nums1[0]:
    			return nums2 + nums1
    		elif nums2[0] > nums1[1]:
    			return nums1 + nums2
    		else:
    			return [nums1[0], nums2[0], nums1[1]]

    	if len(nums2) == 2:
    		if nums1[0] < nums2[0]:
    			return nums1 + nums2
    		elif nums1[0] > nums2[1]:
    			return nums2 + nums1
    		else:
    			return [nums2[0], nums1[0], nums2[1]]

    	if nums2[0] > nums1[0]:
    		return nums1 + nums2
    	else:
    		return nums2 + nums1

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        print nums1
        print nums2
        print "*****************************************"

        if len(nums1) + len(nums2) <= 3:
        	merged  = self.merge(nums1, nums2)
        	m, _, _  = self.getMedian(merged)
        	return m

        m1, l1, u1 = self.getMedian(nums1)
        m2, l2, u2 = self.getMedian(nums2)

        if m1 == m2:
        	return m1
        if l1 == -1:
        	return m2
        if l2 == -1:
        	return m1

        if m1 > m2:
        	new1 = nums1[:l1 + 1]
        	new2 = nums2[u2:]
        elif m1 < m2:
        	new1 = nums1[u1:]
        	new2 = nums2[:l2 + 1]
        else:
        	return m1
        return self.findMedianSortedArrays(new1, new2)

arr1 = [1, 2]
arr2 = [-1, 3]
sol = Solution()

print sol.findMedianSortedArrays(arr1, arr2)