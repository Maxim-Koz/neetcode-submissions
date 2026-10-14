class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # as we are working the numbers, store a list of past differences
        # take the target - current number to get a list of differences
        # as we are checking the current number, if the current number
        # is present as a difference, return the mappings index of that number
        # and our current working index

        diffNums = {}
        for i in range(len(nums)):
            if target - nums[i] in diffNums:
                return [diffNums[target-nums[i]], i]
            else:
                diffNums[nums[i]] = i
        
        return []