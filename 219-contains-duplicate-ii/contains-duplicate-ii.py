class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        freq = {}

        for i in range(len(nums)):
                if nums[i] not in freq:
                    freq[nums[i]] = []
                freq[nums[i]].append(i)    
        for index in freq.values():
            for j in range(len(index)-1):
                if (index[j+1]-index[j]<=k):
                    return True
        return False

        

        