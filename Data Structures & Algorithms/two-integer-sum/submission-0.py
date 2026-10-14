class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            for k in range(len(nums)):
                if nums[n] + nums[k] == target and n != k:
                    return [n,k]
                    