"""
Problem: Quick Sort
Link: <add problem link>

Approach:
    In-place quicksort using Lomuto partition.
    1. Pick the last element as the pivot.
    2. Scan with j; every element <= pivot is swapped into the "smaller"
       region, whose boundary is tracked by i.
    3. Swap the pivot into index i, its final sorted position.
    4. Recurse on the left part (low..i-1) and the right part (i+1..high).
    Base case: low >= high (0 or 1 element).

Time Complexity:  O(n log n) average, O(n^2) worst case (e.g. already sorted
                  input with a fixed last-element pivot)
Space Complexity: O(log n) average recursion stack, O(n) worst case
"""


class Solution:
    def quickSort(self, nums):
        def sortArray(low, high):
            if low >= high:
                return
            pivot = nums[high]
            i = low
            for j in range(low, high):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            sortArray(low, i - 1)
            sortArray(i + 1, high)

        sortArray(0, len(nums) - 1)
        return nums
