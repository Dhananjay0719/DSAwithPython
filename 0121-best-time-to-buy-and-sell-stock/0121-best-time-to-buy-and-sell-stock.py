class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        i=1
        temp=prices[0]
        while i<len(prices):
            if(prices[i]<temp):
                temp=prices[i]
            else:
                maxprofit=max(maxprofit,prices[i]-temp)

            i+=1
        return maxprofit



        