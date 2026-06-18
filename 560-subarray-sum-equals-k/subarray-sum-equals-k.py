class Solution(object):
    def subarraySum(self, nums, k):
        count=0
        curr_sum=0
        freq={0:1}   # summation 0 - occurence 1

        for i in range(len(nums)):
            curr_sum+=nums[i]
            if curr_sum - k in freq:
                count+=freq[curr_sum - k]
            
            freq[curr_sum]=freq.get(curr_sum,0)+1
        return count

