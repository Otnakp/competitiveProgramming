from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median_pos = [(len(nums1) + len(nums2))//2] if (len(nums1) + len(nums2)) % 2 == 1 else [(len(nums1) + len(nums2))//2 - 1, (len(nums1) + len(nums2))//2]
        m1 = binary_search(nums2, median(nums1))
        m2 = binary_search(nums1, nums2[m1])
        print(f"m1: {m1}, m2: {m2}")
        print(f"Median pos: {median_pos}")


def median(nums):
    if len(nums) % 2 == 0:
        return (nums[len(nums)//2] + nums[len(nums) // 2 + 1]) / 2
    return nums[len(nums) // 2]

def binary_search(nums, v):
    def rec_bs(nums, l, r, v):
        if l >= r:
            return r
        m = (l + r) // 2
        if nums[m] == v:
            return m
        elif v > nums[m]:
            return rec_bs(nums, m + 1, r, v)
        elif v < nums[m]:
            return rec_bs(nums, l, m - 1, v)

    return rec_bs(nums, 0, len(nums) - 1, v)

def merge(nums1, nums2):
    return sorted(nums1 + nums2)

# print(binary_search([-2,-1,0,1,2,3,4,7,10], 5))
s = Solution()
nums1 = [-2,0,2,4,7,10,11,12,13]
print(f"Median of nums1: {median(nums1)}")
nums2 = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
print(f"Median of nums2: {median(nums2)}")
print(f"Merged: {merge(nums1,nums2)}")
print(f"Median: {median(merge(nums1,nums2))}")
print(s.findMedianSortedArrays(nums1, nums2))
# -2, -1, 0, 2, 2, 3, 4, 7, 7, 8, 10