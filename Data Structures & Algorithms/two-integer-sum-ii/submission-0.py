class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for start in range(len(numbers)):
            end = len(numbers)-1
            for _ in range(len(numbers)):
                if numbers[end] + numbers[start] == target:
                    return [start+1,end+1]
                elif numbers[end] + numbers[start] < target:
                    break
                end -=1
            