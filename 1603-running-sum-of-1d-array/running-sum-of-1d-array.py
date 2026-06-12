class Solution(object):
    def runningSum(self, nums):
        result = []
        summation = 0
        for i in range(len(nums)):
            summation +=nums[i]
            result.append(summation)
        return result

        