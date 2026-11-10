class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for word in strs:
            s=[0]*26
            for ch in word:
                s[ord(ch)-ord('a')]+=1
            s=tuple(s)
            if s in freq:
                freq[s].append(word)
            else:
                freq[s]=[word]
        return list(freq.values())