class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda x:x[0])
        result = [intervals[0]]

        for start , end in intervals[1:]:
            previous_interval = result[-1] #result[-1]-->recent (rightmost)

            if start<=previous_interval[1]: #previous interval oda first index
                result[-1][1] = max(end , previous_interval[1]) #result[-1][1] -> latest result[-1] oda first(end) index[1]
            else:
                result.append([start,end])
        return result

                

        