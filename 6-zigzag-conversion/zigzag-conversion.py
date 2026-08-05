class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows>=len(s):
            return s
        
        currRows = 0
        rows = [""] * numRows
        goingdown = False


        for i in s:
            rows[currRows]+=i

            if currRows == 0 or currRows == numRows-1:
                goingdown = not goingdown
            
            if goingdown:
                currRows+=1
            else:
                currRows-=1
        return "".join(rows)
    
        