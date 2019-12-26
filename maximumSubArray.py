class Solution:
    def maxSubArray(self, nums):
        maxsum = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] = nums[i] + nums[i-1]
            if nums[i] > maxsum:
                maxsum = nums[i]
        return maxsum


s = Solution()
result = s.maxSubArray([-2, 1])
print(result)
