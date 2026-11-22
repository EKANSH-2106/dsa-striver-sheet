class Solution:
    def leaders(self, nums):
        n=len(nums)
        maxi=nums[n-1]
        ans=[nums[n-1]]
        for i in range(n-2,-1,-1):
            if nums[i]>maxi:
                ans.append(nums[i])
                maxi=nums[i]
        ans.reverse()
        return ans
        
