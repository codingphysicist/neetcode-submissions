class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for i in strs:
            s=[0]*26
            for ch in i:
                s[ord(ch)-ord('a')]+=1
            key=tuple(s)
            group.setdefault(key,[]).append(i)
        return list(group.values())