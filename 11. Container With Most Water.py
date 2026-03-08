class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] > height[r]:
                maximum = max(maximum, (r - l) * height[r])
                r -= 1
            else:
                maximum = max(maximum, (r - l) * height[l])
                l += 1

        return maximum
