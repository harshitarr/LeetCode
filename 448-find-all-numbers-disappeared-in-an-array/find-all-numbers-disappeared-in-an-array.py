class Solution(object):
    def findDisappearedNumbers(self, nums):

        seen = set(nums)
        result = []

        for num in range(1,len(nums)+1):
            if num not in seen:
                result.append(num)
            
        return result

            

        