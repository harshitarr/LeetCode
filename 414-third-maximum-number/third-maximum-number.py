class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))

        if len(nums) < 3:
            return max(nums)

        nums.sort(reverse=True)
        return nums[2]