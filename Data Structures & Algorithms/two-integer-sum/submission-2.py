class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i,num in enumerate(nums):
            freq[num]=i
            
        for i in range(len(nums)):
            j=target-nums[i]
            if j in freq:
                if i !=freq[j]:
                    return [i,freq[j]]