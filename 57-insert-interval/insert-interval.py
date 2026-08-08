class Solution(object):
    def insert(self, intervals, newInterval):

        s , e = newInterval[0] , newInterval[1]
        left = []
        right = []

        for inter in intervals:
            if inter[1]<s:
                left.append(inter)
            elif inter[0]>e:
                right.append(inter)
            else:
                s = min(s,inter[0])
                e =max(e,inter[1])
        return left + [[s, e]] + right

        