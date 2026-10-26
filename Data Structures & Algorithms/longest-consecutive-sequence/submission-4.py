class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best=0
        nums=set(nums)
        for num in nums:
            if num-1 not in nums:
                y=num+1
                while y in nums:
                    y+=1
                best=max(best,y-num)
        return best