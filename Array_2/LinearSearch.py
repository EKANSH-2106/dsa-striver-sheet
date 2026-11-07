
class Solution:
    def linearSearch(self, nums, target):
        n = len(nums)
        for i in range(0, n):
            if nums[i] == target:
                return i
        return -1
