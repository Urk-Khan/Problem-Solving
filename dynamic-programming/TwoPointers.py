###################################################################
# Given a sorted array find if sum of any two elements == X
##################################################################

def naive_solution(arr, val):
	for i in xrange(len(arr)):
		for j in xrange(len(arr)):
			if arr[i] + arr[j] == val:
				return (i, j)
			if arr[i] + arr[j] > val:
				break
	return None
