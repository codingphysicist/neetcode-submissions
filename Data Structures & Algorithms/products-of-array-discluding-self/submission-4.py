class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        p=[1]*(len(nums)+1)
        p[1]=nums[0]
        res=[0]*len(nums)
        s=[1]*(len(nums)+1)
        s[len(nums)-1]=nums[len(nums)-1]
        for i in range(2,len(nums)+1):
            p[i]=p[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            s[i]=s[i+1]*nums[i]
        for i in range(len(nums)):
            res[i]=p[i]*s[i+1]
        return res