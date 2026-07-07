class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars=[]
        l=0
        for i in s:
            if i.isalnum():
                chars.append(i.lower())
        clean_s="".join(chars)
        for r in range(len(clean_s)-1,-1,-1):
            if clean_s[r]!=clean_s[l]:
                return False
            l+=1
        return True