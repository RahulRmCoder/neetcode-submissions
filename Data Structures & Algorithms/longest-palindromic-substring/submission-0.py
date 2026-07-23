class Solution:
    def longestPalindrome(self, s: str) -> str:
        strlen=0
        maxstrlen=0
        maxstr=""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                char = s[i:j]
                if char==char[::-1]:
                    strlen = len(char)
                    if maxstrlen<strlen:
                        maxstrlen=strlen
                        maxstr=char
        return maxstr
        
        