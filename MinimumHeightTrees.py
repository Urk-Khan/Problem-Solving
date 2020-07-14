class Solution(object):

	def createGraph(self, n, input_edges):
		nodes = set()
		edges = {}
		
		for x in xrange(n):
			nodes.add(x)
			edges[x] = set()
		
		for src, dest in input_edges:
			edges[src].add(dest)
			edges[dest].add(src)

		return nodes, edges    

	def runFirstPass(self, node, edges, max_child_dists, child_dists):
		max_child_dists[node] = -1
		if not len(edges[node]): # Leaf
			return 0
		child_dists[node] = {}
		for child in edges[node]:
			edges[child].remove(node)
			dist = self.runFirstPass(child, edges, max_child_dists, child_dists)
			max_child_dists[node] = max(max_child_dists[node], dist)
			child_dists[node][child] = dist
		return max_child_dists[node] + 1

	def max_without_child(self, child, max_distance_from_parent, child_dists):
		maximum = max_distance_from_parent
		for curr in child_dists:
			if curr == child:
				continue
			maximum = max(maximum, child_dists[curr])
		return maximum

	def runSecondPass(self, node, max_distance_from_parent, edges, max_child_dists, child_dists, height_if_root):
		height_if_root[node] = max(max_distance_from_parent, max_child_dists[node]) + 1
		for child in edges[node]:
			self.runSecondPass(child, self.max_without_child(child, max_distance_from_parent, child_dists[node]) + 1, edges, max_child_dists, child_dists, height_if_root)

	def findMinHeightTrees(self, n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		nodes, edges = self.createGraph(n, edges)
		root = nodes.pop()
		nodes.add(root)

		child_dists = {}
		max_child_dists = {}
		height_if_root = {}
		self.runFirstPass(root, edges, max_child_dists, child_dists)
		self.runSecondPass(root, -1, edges, max_child_dists, child_dists, height_if_root)
		minimum = None
		for node in height_if_root:
			if minimum == None:
				minimum = height_if_root[node]
			else:
				minimum = min(minimum, height_if_root[node])

		mins = []

		for node in height_if_root:
			if height_if_root[node] == minimum:
				mins.append(node)
		return mins

n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
sol = Solution()
print sol.findMinHeightTrees(n, edges)