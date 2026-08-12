class Solution(object):
    def minMoves2(self, nums):
        n = len(nums)
        count = 0
        nums.sort()
        median = nums[n//2]

        for num in nums:
            count+=abs(num-median)
        return count
        