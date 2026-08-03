from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        pmap = Counter(p)
        window = Counter()
        left = 0
        res=[]

        for right in range(len(s)):
            window[s[right]]+=1


            if right-left+1>len(p):
                window[s[left]]-=1

                if window[s[left]]==0:
                    del window[s[left]]
                left+=1
        
            if window == pmap:
                res.append(left)
        return res




        