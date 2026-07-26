class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0,len(numbers)-1):
            num=target-numbers[i]
            l=i+1
            r=len(numbers)-1
            while(l<=r):
                mid=(l+r)//2
                if num<numbers[mid]:
                    r=mid-1
                elif num>numbers[mid]:
                    l=mid+1
                elif num==numbers[mid]:
                    return[i+1,mid+1]