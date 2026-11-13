# our approach will be using sliding window/two pointer appraoch where our window represents the optimal day or window to 
# make the transactions

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case handling empty or length = 1 input list
        if not prices or len(prices) == 1:
            return 0
        
        left, right = 0, 1
        best_transaction = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                # Otherwise, calculate profit and update the best seen so far
                transaction = prices[right] - prices[left]
                best_transaction = max(best_transaction, transaction)
            
            # Always move the sell pointer forward
            right += 1
        
        return best_transaction

    