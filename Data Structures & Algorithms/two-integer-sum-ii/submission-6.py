class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            else:
                delta1 = abs(numbers[left + 1] + numbers[right] - target)
                delta2 = abs(numbers[left] + numbers[right - 1] - target)
                if delta1 < delta2:
                    left = left + 1
                else:
                    right = right - 1

        
        return []