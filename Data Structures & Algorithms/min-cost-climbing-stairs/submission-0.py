class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if (len(cost)==0):
            return 0
        elif (len(cost)==1):
            return cost[0]
        elif (len(cost)==2):
            return min(cost[0],cost[1])
        else:
            prev2=cost[0]
            prev=cost[1]
            for i in range(2,len(cost)):
                curr = cost[i]+min(prev2,prev)
                prev2=prev
                prev=curr
            return min(prev,prev2)