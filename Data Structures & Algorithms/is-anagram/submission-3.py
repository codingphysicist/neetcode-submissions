class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s=[0]*26
        hash_t=[0]*26
        for i in s:
            hash_s[ord('a')-ord(i)]+=1
        for i in t:
            hash_t[ord('a')-ord(i)]+=1
        if hash_s==hash_t:
            return True 
        else:
            return False
