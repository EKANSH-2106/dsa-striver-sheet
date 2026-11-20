class Solution:
    def intersection(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        i = 0
        j = 0
        ans = []

        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return ans
