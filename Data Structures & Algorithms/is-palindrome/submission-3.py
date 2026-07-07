class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s=""
        l=0
        for i in s:
            if i.isalnum():
                clean_s+=i.lower()
        for r in range(len(clean_s)-1,-1,-1):
            if r==l:
                return True
            if clean_s[r]!=clean_s[l]:
                return False
            l+=1
        return True