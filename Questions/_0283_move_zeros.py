class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        last_nonzero = 0  # position to place the next nonzero element
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_nonzero], nums[i] = nums[i], nums[last_nonzero]
                last_nonzero += 1