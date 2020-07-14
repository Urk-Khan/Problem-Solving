class Solution(object):
	def createGraph(self, numCourses, prerequisites):
		nodes = set()
		edges = {}
		
		for x in xrange(numCourses):
			nodes.add(x)
			edges[x] = set()
		
		for src, dest in prerequisites:
			edges[src].add(dest)

		return nodes, edges

	def isCyclic_SubTree(self, node, edges, rec_stack, not_visited):
		for dest in edges[node]:

			if dest in rec_stack:
				return True

			if not dest in not_visited:
				continue

			rec_stack.add(dest)
			not_visited.remove(dest)

			ret = self.isCyclic_SubTree(dest, edges, rec_stack, not_visited)
			rec_stack.remove(dest)				
			
			if ret:
				return True

		return False

	def isCyclic(self, nodes, edges):
		not_visited = nodes

		while len(not_visited):
			node = not_visited.pop()
			rec_stack = set()
			rec_stack.add(node)
			if self.isCyclic_SubTree(node, edges, rec_stack, not_visited):
				return True

		return False

	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""

		nodes, edges = self.createGraph(numCourses, prerequisites)
		return not self.isCyclic(nodes, edges)

sol = Solution()
print sol.canFinish(2, [[1, 0], [0, 1]])