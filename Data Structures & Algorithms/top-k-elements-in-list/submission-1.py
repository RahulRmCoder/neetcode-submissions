class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        for i in nums:
            dict1[i]=dict1.get(i,0)+1
        l1=[]
        for value in dict1.values():
            l1.append(value)
        l1=sorted(l1,reverse=True)
        l1=l1[:k]
        l2=[]
        for key in dict1.keys():
            if dict1[key] in l1:
                l2.append(key)
        return l2
                