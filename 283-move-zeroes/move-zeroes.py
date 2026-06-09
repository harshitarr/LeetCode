class Solution(object):
    def moveZeroes(self, nums):
        # step 1 : Move the non Zeros elements in the forward
        k=0 
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k=k+1
                
        #Step 2: Filling the rest with zeros
        for i in range(k,len(nums)):
            nums[i]=0



        