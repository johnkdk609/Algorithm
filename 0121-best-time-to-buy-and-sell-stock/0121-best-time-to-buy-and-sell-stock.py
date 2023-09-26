class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_price = prices[0]

        for price in prices:
            # Update the minimum price if we find a lower price
            if price < min_price:
                min_price = price
            # Calculate the potential profit if we sell at the current price
            potential_profit = price - min_price
            # Update the maximum profit if the potential profit is greater
            if potential_profit > max_profit:
                max_profit = potential_profit

        return max_profit
