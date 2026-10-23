class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        hash_map = set(nums)
        high = 0
        # nums = 2, 20, 4, 10, 3, 4, 5
        count = 0

        # hash_map = 2, 20, 4, 10, 3, 4, 5
        for num in hash_map:
            if num-1 not in hash_map: 
                count = 1 
                while (num + count) in hash_map:
                    count += 1
            
            high = max(high, count)
        return high

        