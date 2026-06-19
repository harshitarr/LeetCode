class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        freq = {}
        count = 0
        
        for num in stones:
            if num not in freq:
                freq[num]=freq.get(num,0)+1
            else:
                freq[num]+=1
        
        for num in jewels:
            if num in freq:
                count+=freq[num]
        return count



        