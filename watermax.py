class Solution:
    def maxArea(self, height):
        maxi = 0
        for i in range(0, len(height)-1):
            for j in range(len(height)-1, i, -1):
                small = height[i] if height[i] < height[j] else height[j]
                area = small * (j-i)
                if area > maxi:
                    maxi = area

        return maxi


s = Solution()
r = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(r)
