class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        result=[]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        bucket=[[] for _ in range(len(nums)+1)]
        for key, value in freq.items():
            bucket[value].append(key)
        for i in range(len(bucket)-1,0,-1):
            if k==0:
                return result
            if not bucket[i]:
                continue
            else:
                for num in bucket[i]:
                    result.append(num)
                    k-=1
                    if k==0:
                        return result
                    
            