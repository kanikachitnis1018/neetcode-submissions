class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()
        # [-1, 0, 1, 2, -1, -4]
        for i in range(n):
            my_set = set()
            for j in range(i+1, n):
                third = 0 - (nums[i] + nums[j])
                if third in my_set:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(nums[j])
        return(list(result))
            