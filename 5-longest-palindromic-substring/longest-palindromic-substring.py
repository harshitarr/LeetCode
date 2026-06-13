class Solution(object):
    def longestPalindrome(self, s):
        start = 0
        maxlen=0

        for i in range(len(s)):
            left = i
            right = i
            while left>=0 and right< len(s) and s[left]==s[right]:
                if maxlen < right-left+1:
                    maxlen = right - left + 1
                    start=left
                left-=1
                right+=1


        for i in range(len(s)):
            left = i
            right = i+1
            while left>=0 and right< len(s) and s[left]==s[right]:
                if maxlen < right-left+1:
                    maxlen = right - left + 1
                    start = left
                left-=1
                right+=1

        return s[start:start+maxlen]


        


            

        



       


        