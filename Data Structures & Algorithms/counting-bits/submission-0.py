class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(0,n+1):
            s = str(bin(i))
            count=0
            for i in s:
                if i=='1':
                    count+=1
            res.append(count)
        return res
        
        
