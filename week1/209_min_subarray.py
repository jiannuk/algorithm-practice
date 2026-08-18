class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0 
        n = len(nums)
        ans = n + 1

        for i in range(n):
