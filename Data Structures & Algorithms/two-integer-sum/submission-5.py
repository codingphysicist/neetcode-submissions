class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        freq={}
        for i in range(0,len(nums)):
            a=target-nums[i]
            if a in freq:
                return [freq[a],i]
            else:
                freq[nums[i]]=i