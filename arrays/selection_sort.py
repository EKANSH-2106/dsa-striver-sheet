# Problem: Selection Sort
# Link: <paste the problem link here>
# Approach: Repeatedly find the smallest element in the unsorted part
#           and swap it into the next position of the sorted part.
# Time Complexity: O(n^2) in all cases (best, average, worst)
# Space Complexity: O(1), sorts in place

class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums
