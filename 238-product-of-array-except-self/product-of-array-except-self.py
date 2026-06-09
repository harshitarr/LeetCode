class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        arr=[1]*n

        prefix = 1

        for i in range(n):
            arr[i]=prefix
            prefix*=nums[i]
        
        suffix = 1

        for i in range(n-1,-1,-1):
            arr[i]*=suffix
            suffix*=nums[i]
        
        return arr
