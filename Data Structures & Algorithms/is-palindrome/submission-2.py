class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        strsclean=""
        strsrev=""
        
        for i in s:
            if i.isalnum():
                strsclean+= i.lower()
        
        for i in range(len(strsclean)-1,-1,-1):
            if strsclean[i].isalnum():
                strsrev+=strsclean[i]
        
        if strsclean == strsrev:
            return True
        return False

        