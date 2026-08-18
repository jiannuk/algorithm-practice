class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        n = len(nums)
        for i in range(1,n):
            if nums[i] != 0:
                nums[k] = nums[i]
                k +=1
        for j in range(k,n):
            nums[j] = 0
