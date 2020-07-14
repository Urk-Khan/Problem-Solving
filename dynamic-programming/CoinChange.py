# import numpy as np
# from sys import maxint
# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         ln = len(coins)
#         table = np.zeros((ln, amount + 1), dtype=int)
        
#         for n in xrange(ln):
#             for am in xrange(amount + 1):
#                 if n == 0:
#                     if am == 0:
#                         table[n][am] = 0
#                     elif coins[n] <= am and am % coins[n] == 0:
#                         table[n][am] = am/coins[n]
#                     else:
#                         table[n][am] = maxint
#                     continue

#                 if am == 0:
#                     table[n][am] = 0
#                     continue
                
#                 minimum = table[n - 1][am]
#                 coins_to_add = 1
#                 while coins_to_add * coins[n] <= am:
#                     if table[n - 1][am - coins_to_add * coins[n]] == maxint:
#                         coins_to_add += 1
#                         continue
#                     score = coins_to_add + table[n - 1][am - coins_to_add * coins[n]]
#                     minimum = min(score, minimum)
#                     coins_to_add += 1
#                 table[n][am] = minimum
#         return -1 if table[ln - 1][amount] == maxint else table[ln - 1][amount]

class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        print dp
        return dp[amount] if dp[amount] != float('inf') else -1 

coins = [1, 2, 5]
amount = 11
sol = Solution()
print sol.coinChange(coins, amount)