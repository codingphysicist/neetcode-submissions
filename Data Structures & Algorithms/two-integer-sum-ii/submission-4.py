class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        for r in range(0,len(numbers)):
            mid=(r+len(numbers))//2
            num =target-numbers[r]
            if num ==numbers[mid]:
                return [r+1,mid+1]
            elif num<numbers[mid]:
                for i in range(r+1,mid):
                    if num==numbers[i]:
                        return[r+1,i+1]
            elif num>numbers[mid]:
                for i in range(mid+1,len(numbers)):
                    if num==numbers[i]:
                        return[r+1,i+1]