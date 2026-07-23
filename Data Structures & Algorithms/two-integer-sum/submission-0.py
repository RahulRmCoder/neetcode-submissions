class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictn={}

        for i,num in enumerate(nums):
            complement= target - num
            if complement in dictn:
                return [dictn[complement],i]
            dictn[num]=i 
