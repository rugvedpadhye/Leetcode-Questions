class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        result=0
        n=len(nums)
        nums.sort()
        for i in range(0,n,2):
           result+=nums[i]
        return result 