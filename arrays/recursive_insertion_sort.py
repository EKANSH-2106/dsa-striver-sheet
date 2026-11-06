
class Solution:
    def insertionSort(self, nums):
        def insert(n):
            if n <= 0:
                return

            insert(n - 1)
            key = nums[n]

            def shift(j):
                if j < 0 or nums[j] <= key:
                    nums[j + 1] = key
                    return

                nums[j + 1] = nums[j]
                shift(j - 1)

            shift(n - 1)

        if nums:
            insert(len(nums) - 1)

        return nums
