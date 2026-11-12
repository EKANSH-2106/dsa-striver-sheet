
class Solution:
    def secondLargestElement(self, nums):
        largest = None
        second_largest = None

        for num in nums:
            if largest is None or num > largest:
                second_largest = largest
                largest = num

            elif num < largest and (
                second_largest is None or num > second_largest
            ):
                second_largest = num

        return -1 if second_largest is None else second_largest
