class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq=[0]*26
        for i in range(0,len(s)):
            freq[ord(s[i])-ord('a')]+=1
        for i in range(0,len(t)):
            freq[ord(t[i])-ord('a')]-=1
        return freq==[0]*26