class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # base case: if index == len(nums): return 0
        # 1. if nums[index] > prev: seq1 = 1 + self.recursive() (include current element)
        # 2. if nums[index] > prev: seq2 = self.recursive() (skip current element)
        # return max(seq1, seq2)

        # return self.recursive(nums, 0, -math.inf)

        return self.bottomUp(nums)
    
    def recursive(self, nums, index, prev):
        if index == len(nums): return 0

        seq1, seq2 = -math.inf, -math.inf
        if nums[index] > prev: seq1 = 1 + self.recursive(nums, index + 1, nums[index])
        seq2 = self.recursive(nums, index + 1, prev)

        return max(seq1, seq2)
    
    def bottomUp(self, nums):
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
