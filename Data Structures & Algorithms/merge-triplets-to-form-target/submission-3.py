class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        maps= set()
        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            else:
                for i,v in enumerate(t):
                    if v==target[i]:
                        maps.add(i)
        if len(maps)==3:
            return True
        return False