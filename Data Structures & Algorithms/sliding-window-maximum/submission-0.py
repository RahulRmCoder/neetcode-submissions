class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=0
        maxSum=0
        res=[]
        while r <len(nums)+1:
            if (r-l+1)<=k:
                r+=1
            else:
                l1=nums[l:r]
                maxSum = max(l1)
                res.append(maxSum)
                l+=1
        return res
            
                
        