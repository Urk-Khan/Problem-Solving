class Solution(object):

	def getNoIncoming(self, incoming):
		for c in incoming:
			if len(incoming[c]) == 0:
				return c
		return None

	def removeFromIncoming(self, c, incoming, outgoing):
		for t in outgoing[c]:
			incoming[t].remove(c)
		del incoming[c]
		del outgoing[c]

	def alienOrder(self, words):
		"""
		:type words: List[str]
		:rtype: str
		"""

		if len(words) == 1:
			return words[0]


		incoming = {}
		outgoing = {}
		vocab_len = 0
		for word in words:
			for c in word:
				if not c in incoming:
					incoming[c] = set()
					outgoing[c] = set()
					vocab_len += 1
		idx = 1
		while idx < len(words):
			prev = words[idx - 1]
			curr = words[idx]
			for i, cp in enumerate(prev):
				if i >= len(curr):
					return ""
				cc = curr[i]
				if cp != cc:
					incoming[cc].add(cp)
					outgoing[cp].add(cc)
					break
			idx += 1

		curr = self.getNoIncoming(incoming)
		order = ""
		while curr != None:
			order += curr
			self.removeFromIncoming(curr, incoming, outgoing)
			curr = self.getNoIncoming(incoming)
		if len(order) != vocab_len:
			return ""
		return order

sol = Solution()

# ls = [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]

ls = [
"abc",
"ab"
]

print sol.alienOrder(ls)