class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=set(nums)
        a=list(a)
        a.sort()
        nums.sort()
        if a!=nums:
            return True
        else:
            return False

        