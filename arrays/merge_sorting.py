# Problem: 1020. Merge Sorting
# Link: <paste problem link>
# Approach: Divide and conquer. Split the array in half, recursively sort
#           each half, then merge by repeatedly taking the smaller front element.
# Time Complexity: O(n^2) because pop(0) is O(n); O(n log n) if using pointers/deque
# Space Complexity: O(n)

class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left, right = self.sortArray(nums[:mid]), self.sortArray(nums[mid:])

        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        return merged + left + right
