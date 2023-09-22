from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        i0 = 0
        i1 = len(nums) - 1
        c = 0
        take_max = True
        while x > 0 and i0 <= i1:
            print(nums[i0:i1])
            print(x)
            if nums[i0] == nums[i1] and nums[i0] <= x:
                x -= nums[i1]
                c += 1
                i1 += 1
                if x == 0:
                    return c
                if x > 0 and nums[i1] <= x:
                    x -= nums[i1]
                    i1 += 1
                    c += 1
            elif nums[i0] > nums[i1] and nums[i0] <= x:
                x -= nums[i0]
                i0 += 1
                c += 1
            elif nums[i0] < nums[i1] and nums[i1] <= x:
                x -= nums[i1]
                i1 -= 1
                c += 1
            elif nums[i0] < nums[i1] and nums[i0] <= x:
                x -= nums[i0]
                i0 += 1
                c += 1
            elif nums[i0] > nums[i1] and nums[i1] <= x:
                x -= nums[i1]
                i1 -= 1
                c += 1
            if nums[i0] > x and nums[i1] > x:
                if x == 0:
                    return c
                else:
                    return -1
            if x == 0:
                return c
        if x == 0:
            return c
        return -1
    def my_max(self, nums, i0, i1):
        if nums[i0] >= nums[i1]:
            return i0
        return i1

s = Solution()
print(s.minOperations(
[8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309],
    134365))