class Solution(object):
    def isAnagram(self, s, t):
        freq = {}

        for ch in s:
            freq[ch]=freq.get(ch,0)+1

        for ch in t:
            if ch not in freq:
                return False
            freq[ch]-=1
        
        for count in freq.values():
            if count!=0:
                return False
        return True


        