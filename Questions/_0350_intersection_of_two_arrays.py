from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection_counter = Counter(nums1) & Counter(nums2)
        result = list(intersection_counter.elements())
        return result