class Solution(object):
	def createGraph(self, n, edges):
		nodes = set([x for x in xrange(n)])
		adj = [(x, set()) for x in xrange(n)]
		adj = dict(adj)
		for n1, n2 in edges:
			adj[n1].add(n2)
			adj[n2].add(n1)
		return nodes, adj

	def runDFS(self, node, adj, not_visited):
		for e in adj[node]:
			if not e in not_visited:
				continue
			not_visited.remove(e)
			self.runDFS(e, adj, not_visited)

	def countComponents(self, n, edges):
		nodes, adj = self.createGraph(n, edges)
		not_visited = nodes
		num_iters = 0
		while len(not_visited):
			node = not_visited.pop()
			self.runDFS(node, adj, not_visited)
			num_iters += 1
		return num_iters

n = 5
edges = [[0, 1], [1, 2], [3, 4]]
sol = Solution()
print sol.countComponents(n, edges)