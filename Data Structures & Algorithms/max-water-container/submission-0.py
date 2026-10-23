class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxcap = 0
        for i in range(n):
            for j in range(i+1, n):
                width = j - i
                maxcap = max(maxcap, width * min(heights[i], heights[j]))
        return maxcap