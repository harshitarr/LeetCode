class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
            
            if freq[num]>n/2:
                return num



        