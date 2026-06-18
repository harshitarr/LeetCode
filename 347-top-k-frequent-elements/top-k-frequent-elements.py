class Solution(object):
    def topKFrequent(self, nums, k):
        
        # Step 1: Count frequency
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: Create buckets
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num, count in freq.items():
            bucket[count].append(num)
        
        # Step 3: Collect top k frequent
        result = []
        
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result