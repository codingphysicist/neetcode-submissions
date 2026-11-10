class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res=[]
        bucket=[[] for i in range(len(nums)+1)]
        for num in nums:
            freq[num]=1+freq.get(num,0)
        for key, value in freq.items():
            bucket[value].append(key)
        for l in reversed(bucket):
            if k==0:
                return res
            for num in l:
                if k==0:
                    return res
                res.append(num)
                k-=1