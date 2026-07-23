class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left in range(len(nums)):
            for right in range(left+1,len(nums)):
                sum1 = nums[left] + nums[right]
                if target==sum1:
                    return [left,right]
                
        
