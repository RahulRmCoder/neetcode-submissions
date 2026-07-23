class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count1={}
        # count2={}
        # for i in s:
        #     count1[i] = count1.get(i,0)+1
        # for i in t:
        #     count2[i] = count2.get(i,0)+1
        # if count1==count2:
        #     return True
        # return False

        s1 = "".join(sorted(s))
        s2 = "".join(sorted(t))
        return s1==s2