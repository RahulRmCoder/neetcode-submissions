class Solution:
    def hammingWeight(self, n: int) -> int:
        n=bin(n)
        s = str(n)
        s1=s[2:]

        count=0
        
        for i in s1:
            if i=='1':
                count+=1
        return count