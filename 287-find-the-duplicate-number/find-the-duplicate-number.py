class Solution(object):
    def findDuplicate(self, nums):
        freq = {}

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
            if freq[num]>1:
                return num
                

        