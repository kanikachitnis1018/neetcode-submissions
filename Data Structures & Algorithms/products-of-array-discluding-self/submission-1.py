class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            products[i] = prefix
            prefix *= nums[i]

        post = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= post
            post *= nums[i]
        
        return products

# 1,2,3,4
# 1,2,6,24
# 1
            
