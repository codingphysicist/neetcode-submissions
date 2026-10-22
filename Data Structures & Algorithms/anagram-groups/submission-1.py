class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for i in strs:
            a=[0]*26
            for ch in i:
                a[ord(ch)-ord('a')]+=1
            a=tuple(a)
            if a in freq:
                freq[a].append(i)
            else:
                freq[a]=[i]
        return list(freq.values())
            