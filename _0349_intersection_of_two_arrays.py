class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
      result = list(set(nums1).intersection(nums2))
      return result 