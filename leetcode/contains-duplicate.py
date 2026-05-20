class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    # brute force
    #    for i in range (len(nums)):
    #        target = nums[i]
    #        for j in range (i+1, len(nums)):
    #            if nums[j] == target:
    #                return True
            
    #    return False
    # we can use sets for this since sets only stotre unique
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False