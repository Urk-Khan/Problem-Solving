class Solution(object):
    
    def createGraph(self, equations, values):
        nodes = set()
        edges = {}
        for idx, [num, den] in enumerate(equations):
            if not num in nodes:
                nodes.add(num)
                edges[num] = set()
            if not den in nodes:
                nodes.add(den)
                edges[den] = set()
            edges[num].add((den, values[idx]))
            edges[den].add((num, 1/values[idx]))
        return nodes, edges
    
                           
    def findMultiplesTo(self, src, dest, edges, visited):
        if src in visited:
            return False, -1.0 
        visited.add(src)
        if src == dest:
            return True, 1.0
        for [e, w] in edges[src]:
            found, val = self.findMultiplesTo(e, dest, edges, visited)
            if found:
                return True, w * val
        return False, -1.0
                           
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        nodes, edges = self.createGraph(equations, values)
        
        results = []
        for [num, den] in queries:
            if not num in nodes or not den in nodes:
                results.append(-1.0)
                continue        
            visited = set()
            found, val = self.findMultiplesTo(num, den, edges, visited)
            if found:
                results.append(val)
            else:
                results.append(-1.0)
                           
        return results

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

sol = Solution()

print sol.calcEquation(equations, values, queries)