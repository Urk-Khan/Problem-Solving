# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

	def merge2Lists(self, head1, head2):
		curr1 = head1
		curr2 = head2
		head = None
		curr = None
		if head1 == None and head2 == None:
			return None
		elif head1 == None:
			return head2
		elif head2 == None:
			return head1

		while curr1 != None and curr2 != None:
			if curr1.val < curr2.val:
				node_to_add = curr1
				curr1 = curr1.next
			else:
				node_to_add = curr2
				curr2 = curr2.next
			if head == None:
				head = node_to_add
				curr = node_to_add
			else:
				curr.next = node_to_add
				curr = node_to_add
		if curr1 == None:
			curr.next = curr2
		else:
			curr.next = curr1
		return head

	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		if len(lists) == 0:
			return None
		if len(lists) == 1:
			return lists[0]
		if len(lists) == 2:
			return self.merge2Lists(lists[0], lists[1])

		mid = len(lists)/2
		lhs = self.mergeKLists(lists[:mid])
		rhs = self.mergeKLists(lists[mid:])
		return self.merge2Lists(lhs, rhs)

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
		print head.val
		head = head.next

# lists = [create_ll([1,4,5]),create_ll([1,3,4]),create_ll([2,6])]
lists = [None, create_ll([1])]
sol = Solution()
print_ll(sol.mergeKLists(lists))