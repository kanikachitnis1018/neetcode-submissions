class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    # [2,20,4,10,3,4,5]   
        res = set(nums)
    # [2,20,4,10,3,5]
        longest = 0

        for nums in res:
            if (nums-1) not in res:
                length = 1
                while (nums+length) in res:
                    length += 1
                longest = max(length, longest)
        return longest