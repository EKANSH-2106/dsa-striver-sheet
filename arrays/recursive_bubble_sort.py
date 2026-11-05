class Solution:
    def bubbleSort(self, nums):
        n = len(nums)

        def bubblePass(j, n):
            if j == n - 1:
                return

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

            bubblePass(j + 1, n)

        def recursiveSort(n):
            if n <= 1:
                return

            bubblePass(0, n)
            recursiveSort(n - 1)

        recursiveSort(n)
        return nums
