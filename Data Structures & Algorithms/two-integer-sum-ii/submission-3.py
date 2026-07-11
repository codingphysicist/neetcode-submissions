class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mid = len(numbers) // 2

        for r in range(len(numbers)):
            num = target - numbers[r]

            if num == numbers[mid]:
                return [r + 1, mid + 1]

            if num < numbers[mid]:
                for i in range(r + 1, mid):
                    if numbers[i] == num:
                        return [r + 1, i + 1]
            else:
                for i in range(max(mid + 1, r + 1), len(numbers)):
                    if numbers[i] == num:
                        return [r + 1, i + 1]