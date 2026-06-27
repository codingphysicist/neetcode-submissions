class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my=set(nums)
        if len(my)==len(nums):
            return False 
        else:
            return True