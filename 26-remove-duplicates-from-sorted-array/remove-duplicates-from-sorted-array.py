class Solution(object):
    def removeDuplicates(self, nums):
        uni = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[uni]:
                uni+=1
                nums[uni]=nums[i]
        return uni+1
            




            

        