class Solution(object):
    def twoSum(self, nums, target):
        sum = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sum = nums[i]+nums[j]
                if sum == target:
                    return [i,j]
                   
                


        