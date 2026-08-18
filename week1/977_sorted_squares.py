class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k = 0
        for i in nums:
            j = i * i
            nums[k]=j
            k += 1
        return sorted(nums)
