'''House Robber

You are a professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed, the only constraint stopping you from robbing each of
them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the
maximum amount of money you can rob tonight without alerting the police.'''

class Solution:
  def rob(self, nums):
    n = len(nums)
    if n == 0:
      return 0
    if n == 1:
      return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
      dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]

solution = Solution()
nums1 = [1, 2, 3, 1]
print("Maximum amount you can rob:", solution.rob (nums1)) # Output: 4
nums2 = [2, 7, 9, 3, 1]
print("Maximum amount you can rob:", solution.rob (nums2)) # Output: 12
