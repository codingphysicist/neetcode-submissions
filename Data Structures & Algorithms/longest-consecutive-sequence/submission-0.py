class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq={}
        s=set(nums)
        result=0
        for num in s:
            if num-1 in s:
                continue
            else:
                freq[num]=1
        for key in freq:
            current=key
            while True:
                if current+1 in s:
                    freq[key]+=1
                    current+=1
                else:
                    if freq[key]>result:
                        result=freq[key]
                    break
        return result