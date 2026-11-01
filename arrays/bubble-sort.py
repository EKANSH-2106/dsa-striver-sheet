# Problem: Bubble Sort (467)
# Link: <paste problem link here>
# Approach: Repeatedly compare adjacent elements and swap them if they are
#           out of order. After each pass the largest remaining element
#           settles at the end, so the inner loop shrinks by one each pass.
#           If a pass makes no swaps, the array is sorted and we stop early.
# Time: O(n^2) worst/average, O(n) best (already sorted)
# Space: O(1)

class Solution:
    def bubbleSort(self, nums):
        n = len(nums)

        for i in range(n - 1):
            swapped = False

            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True

            if not swapped:
                break

        return nums
