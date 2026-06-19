class Solution(object):
    def findDifference(self, nums1, nums2):

        # initally it is in list so convert them first into set
        set1 = set(nums1)
        set2 = set(nums2)

        diff1 = list(set1 - set2)
        diff2 = list(set2 - set1)

        return [diff1 , diff2]

        