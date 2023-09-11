from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        results = [0 for _ in range(len(nums))]
        # Fail. My solution works but is not fast enough


    def smallestSubarrays_slow(self, nums: List[int]) -> List[int]:
        results = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            t = nums[i]
            j = i + 1
            size = 1
            while j < len(nums) and t | nums[j] >= t:
                if t | nums[j] > t:
                    size = j - i + 1
                t = t | nums[j]
                j += 1
            results[i] = size
        return results


s = Solution()
nums = [1, 0, 2, 1, 3]
print(nums)
print(s.smallestSubarrays(nums))
