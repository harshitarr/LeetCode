class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        arr = nums
        for i in range(len(arr)):
            if arr[i]!=i:
                return i
        return len(nums)


            
            
        