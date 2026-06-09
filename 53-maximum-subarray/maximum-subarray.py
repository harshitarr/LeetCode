class Solution(object):
    def maxSubArray(self, nums):
        curr = nums[0]
        maxSum= nums[0]

        for i in range(1,len(nums)):
            curr = max(nums[i],curr+nums[i])
            maxSum = max(maxSum , curr)
        return maxSum

        