class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        for i in range(len(nums)):
            j = 0
            product = 1
            while j < len(nums):
                if j != i:
                    product = product * nums[j]
                else:
                    pass
                j += 1
            products.append(product)
        return products