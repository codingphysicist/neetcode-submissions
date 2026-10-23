class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for i in strs:
            freq=[0]*26
            for ch in i:
                freq[ord(ch)-ord('a')]+=1
            freq=tuple(freq)
            if freq in group:
                group[freq].append(i)
            else:
                group[freq]=[i]
        return list(group.values())