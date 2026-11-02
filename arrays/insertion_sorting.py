# Problem: 1013. Insertion Sorting
# Link: <paste problem link here>
# Approach: Keep the left part sorted. For each element (key), shift larger
#           elements in the sorted part one step right, then insert key
#           into the gap.
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1

            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = key

        return nums
