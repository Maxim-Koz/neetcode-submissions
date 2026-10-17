class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        found = False
        while left <= right:
            pos = int((right - left)/2) + left
            if target < nums[pos]:
                right = pos - 1
            elif target > nums[pos]:
                left = pos + 1
            elif target == nums[pos]:
                return pos
        return -1
        
