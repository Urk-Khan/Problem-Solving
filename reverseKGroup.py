# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
	def reverseList(self, head):
		curr = head
		prev = None

		while curr != None:
			tmp = curr.next
			curr.next = prev
			prev = curr
			curr = tmp

		return prev

	def reverseKGroup(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		if k <= 1:
			return head
		prev_tail = None
		curr_list_start = head
		curr = head
		idx = 1
		while curr != None:
			if idx == k:
				next_node = curr.next
				curr.next = None
				self.reverseList(curr_list_start)
				curr_list_start.next = next_node
				if prev_tail != None:
					prev_tail.next = curr
				else:
					head = curr
				prev_tail = curr_list_start
				curr_list_start = next_node
				idx = 1
				curr = next_node
			else:
				idx += 1
				curr = curr.next
		return head



def create_ll(ls):
	head = ListNode(ls[0])
	curr = head
	for val in ls[1:]:
		node = ListNode(val)
		curr.next = node
		curr = node
	return head

def print_ll(head):
	while head != None:
		print head.val,
		head = head.next
	print

ll = create_ll([1, 2, 3, 4, 5])

sol = Solution()
print_ll(sol.reverseKGroup(ll, 3))