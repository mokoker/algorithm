class Solution:
    def findDisappearedNumbers(self, nums):
        results = []
        sorty = sorted(nums)
        for i in range(1, len(sorty)):
            if sorty[i] - sorty[i-1] > 1:
                for j in range(sorty[i-1]+1, sorty[i]):
                    results.append(j)
        return results


s = Solution()
result = s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
print(result)
