import sys

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1 = -float("inf")
        hold2 = -float("inf")
        release1 = 0
        release2 = 0
        for i in prices:
            release2 = max(release2, hold2+i)
            hold2 = max(hold2, release1-i)
            release1 = max(release1, hold1+i)
            hold1 = max(hold1, -i)
        return release2
    
    def maxProfit0(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = -sys.maxsize
        sell1 = 0
        buy2 = -sys.maxsize
        sell2 = 0
        for p in prices:
            buy1 = buy1 if buy1 > -p else -p
            sell1 = sell1 if sell1 >  buy1+p else buy1+p
            buy2 = buy2 if buy2 > sell1-p else sell1-p
            sell2 = sell2 if sell2 > buy2+p else buy2+p
        return sell2
    