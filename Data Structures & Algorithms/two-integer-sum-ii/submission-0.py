class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        numdict={}

        for i,num in enumerate(numbers):
            complement = target-num
            if complement in numdict:
                return [numdict[complement]+1,i+1]
            numdict[num]=i