import math

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    
	def read_val(self, ll):
		val = 0
		idx = 0
		while ll != None:
			val += ll.val * 10 ** idx
			idx += 1
			ll = ll.next
		return val
	def create_ll(self, num):
		if num == 0:
			return ListNode(0)
		idx = int(math.floor(math.log10(num)))
		prev = None
		tot = 0
		while idx >= 0:
			val = (num/(10 ** idx)) % 10
			idx -= 1
			prev = ListNode(val, prev)

		return prev

	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""

		return self.create_ll(self.read_val(l1) + self.read_val(l2))


def printll(ll):
	while ll != None:
		print ll.val
		ll = ll.next
sol = Solution()

n11 = ListNode(0)
n12 = ListNode(8, n11)
n13 = ListNode(6, n12)
n14 = ListNode(0, n13)
n15 = ListNode(1, n14)

n21 = ListNode(0)
n22 = ListNode(1, n21)
n23 = ListNode(1, n22)
n24 = ListNode(1, n23)
n25 = ListNode(1, n24)

printll(sol.addTwoNumbers(n11, n21))