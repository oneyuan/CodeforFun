import heapq

class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
            return 0
        if k > len(prices)/2:
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            return res
                
        hold = [-float("inf") for _ in range(k)]
        release = [0 for _ in range(k)]
        for i in prices:
            for j in range(k-1, -1, -1):
                release[j] = release[j] if release[j] > hold[j] + i else hold[j]+i
                if j > 0:
                    hold[j] = hold[j] if hold[j] > release[j-1]-i else release[j-1]-i
                else:
                    hold[j] = hold[j] if hold[j] > -i else -i
        return release[-1]
    
    def maxProfit0(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        if k <= 0 or N<=1: return 0

        #if k >= N/2, then you can make maximum number of transactions; greedy
        if k >= N//2:
            ans = 0
            for i in range(N-1):
                diff = prices[i+1] - prices[i]
                if diff > 0: ans+= diff
            return ans
        
        v = p = 0
        pairs, profits = [], []
        
        while p < N:
            
            v = p
            while v < N - 1 and prices[v+1] <= prices[v]: v += 1

            p = v+1
            while p < N and prices[p] >= prices[p-1]: p += 1

            
            while pairs and prices[v] < prices[pairs[-1][0]]:
                heapq.heappush(profits, prices[pairs[-1][0]] - prices[pairs[-1][1] - 1])
                pairs.pop()

            
            # If prices[v1]<prices[v2] and prices[p1]<prices[p2], 
            # then it is meaningful to combine the two transactions
            # update (v1, p1) to (v1, p2), and save the profit of (v2, p1)
            while pairs and prices[p-1] >= prices[pairs[-1][1] - 1]:
                heapq.heappush(profits, prices[v] - prices[pairs[-1][1] - 1])
                v = pairs[-1][0]
                pairs.pop()

            pairs.append((v, p))

        while pairs:
            heapq.heappush(profits, prices[pairs[-1][0]] - prices[pairs[-1][1] - 1])
            pairs.pop()


        ans = 0
        while k != 0 and profits:
            ans += -heapq.heappop(profits)
            k -= 1
        return ans
        