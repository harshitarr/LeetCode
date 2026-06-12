class Solution(object):
    def sortedSquares(self, nums):
        result = []
        for i in range(len(nums)):
            square = nums[i]*nums[i]
            result.append(square)
            result.sort()
        return result
            
        