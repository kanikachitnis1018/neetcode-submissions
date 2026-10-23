class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:  # if the first half is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    nums[mid] < target
                    low = mid + 1

            else:                       # if nums[mid] < nums[high], then the 2nd half of the array is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else: 
                    nums[mid] > target
                    high = mid - 1
   
        return -1 