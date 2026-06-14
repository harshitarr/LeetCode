class Solution(object):
    def wordPattern(self, pattern, s):
        map1 = []
        map2 = []
        s = s.split()

        for idx in pattern:
            map1.append(pattern.index(idx))
        for idx in s:
            map2.append(s.index(idx))
        if map1 == map2:
            return True
        return False

        