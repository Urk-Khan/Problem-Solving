class Solution(object):
    def createGraph(self, n, edges):
    	nodes = set([x for x in xrange(n)])
    	adj = [(x, set()) for x in xrange(n)]
    	adj = dict(adj)
    	for n1, n2 in edges:
    		adj[n1].add(n2)
    		adj[n2].add(n1)

    	return nodes, adj

    def isCyclic(self, node, stack, adj, not_visited):
    	for e in adj[node]:
    		if e in stack:
    			return True
    		adj[e].remove(node)
    		not_visited.remove(e)
    		stack.add(e)	
    		if self.isCyclic(e, stack, adj, not_visited):
    			return True
    	return False

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        nodes, adj = self.createGraph(n, edges)
        not_visited = nodes

    	node = not_visited.pop()
    	stack = set([node])
    	if self.isCyclic(node, stack, adj, not_visited):
    		return False
    	if len(not_visited):
    		return False
        return True

n = 5
edges = [[0,1], [2, 3]]

sol = Solution()
print sol.validTree(n, edges)