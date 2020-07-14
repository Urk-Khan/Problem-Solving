class Solution(object):
	def createGraph(self, numCourses, prerequisites):
		nodes = set()
		source_with = {}
		dest_with = {}

		for x in xrange(numCourses):
			nodes.add(x)
			source_with[x] = set()
			dest_with[x] = set()
		
		for dest, src in prerequisites:
			source_with[src].add(dest)
			dest_with[dest].add(src)

		return nodes, source_with, dest_with

	def no_incoming(self, dest_with):
		for dest in dest_with:
			if len(dest_with[dest]) == 0:
				return dest
		return None

	def remove_src(self, node, source_with, dest_with):
		
		for dest in source_with[node]:
			dest_with[dest].remove(node)
		for src in dest_with[node]:
			source_with[src].remove(node)

		del dest_with[node]
		del source_with[node]

	def findOrder(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: List[int]
		"""

		nodes, source_with, dest_with = self.createGraph(numCourses, prerequisites)
		order = []

		src = self.no_incoming(dest_with)
		while src != None:
			order.append(src)
			self.remove_src(src, source_with, dest_with)
			src = self.no_incoming(dest_with)

		if len(order) != numCourses:
			return []

		return order

sol = Solution()
print sol.findOrder(2, [[1, 0]])