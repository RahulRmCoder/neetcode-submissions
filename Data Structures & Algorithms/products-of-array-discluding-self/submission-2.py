class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # l=[]
        # for i in range(len(nums)):
        #     a = nums[i]
        #     p=1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             p*=nums[j]
        #     l.append(p)
        # return l

        n= len(nums)
        res = [1]*len(nums)

        prefix=1
        for i in range(n):
            res[i]=prefix
            prefix*=nums[i]
        
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix *= nums[i]
        
        return res

            
