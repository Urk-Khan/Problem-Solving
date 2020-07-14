class Solution(object):
    def get_comp_up_to(self, prices, comp):
        comp_up_to = [prices[0]]
        for price in prices[1:]:
            comp_up_to.append(comp(price, comp_up_to[-1]))
        return comp_up_to
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_up_to = self.get_comp_up_to(prices, min)
        prices.reverse()
        max_from = self.get_comp_up_to(prices, max)
        max_from.reverse()
        print min_up_to
        print max_from

        maximum_profit = 0     
        for idx, buy_at in enumerate(min_up_to[:-1]):
            maximum_profit = max(max_from[idx + 1] - buy_at, maximum_profit)
        return maximum_profit

arr = [7,1,5,3,6,4]
sol = Solution()
print sol.maxProfit(arr)