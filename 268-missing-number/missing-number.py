class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected = n*(n+1)//2
        actual = 0
        for x in nums:
            actual+=x
        return expected - actual


            
            
        