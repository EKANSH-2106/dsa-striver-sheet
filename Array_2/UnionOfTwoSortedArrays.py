class Solution:
    def unionArray(self, nums1, nums2):
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
                ans.append(nums1[i])
                i += 1

            else:
                ans.append(nums2[j])
                j += 1

        while i < n1:
            ans.append(nums1[i])
            i += 1

        while j < n2:
            ans.append(nums2[j])
            j += 1

        return ans
