class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums==[]:
            return 0
        nums =set(nums)
        arr=[]
        for num in nums:
            if num-1 not in nums:
                if num+1 in nums:
                    arr.append(num)
        
        freq={}
        if arr==[]:
            return 1
        for num in arr:
            count=1
            a=num
            while True:
                a=a+1
                if a in nums:
                    count+=1
                else:
                    break
            freq[num]=count
        return max(freq.values())