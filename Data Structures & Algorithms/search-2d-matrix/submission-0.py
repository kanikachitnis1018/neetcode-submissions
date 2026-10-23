class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols
        low = 0
        high = total - 1

        while low <= high:
            mid = (low + high) // 2
            i = mid // cols
            j = mid % cols
            mid_value = matrix[i][j]

            if mid_value == target:
                return True
            elif mid_value < target:
                low = mid + 1
            else:
                high = mid - 1
        return False