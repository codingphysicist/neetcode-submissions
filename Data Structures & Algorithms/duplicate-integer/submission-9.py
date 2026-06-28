class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash=[0]*((10**5)+1)
        for i in nums:
            hash[i]+=1
        for i in hash:
            if i>1:
                return True
        return False