from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        q = deque()
        result = [0]*(n-k+1)

        for right in range(n):
            while q and q[0]<=right-k:
                q.popleft()
            while q and nums[q[-1]]<nums[right]:
                q.pop()
            q.append(right)

            if right>=k-1:
                result[right-k+1]=nums[q[0]]
        return result



        