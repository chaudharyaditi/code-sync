class Solution(object):
# brute force:
#    def twoSum(self, nums, target):
#        for i in range(len(nums)):
#            for j in range(i + 1, len(nums)):
#                if nums[i] + nums[j] == target:
#                    return [i, j]
# instead of searching through each pair, we could store numbers we've already seen and instantly check if needed partner exists
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return [seen[needed], i]
            seen[nums[i]] = i