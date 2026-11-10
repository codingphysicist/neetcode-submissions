class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check={}
        for i in range(len(nums)):
            num=target-nums[i]
            if num in check:
                return [check[num],i]
            else:
                check[nums[i]]=i