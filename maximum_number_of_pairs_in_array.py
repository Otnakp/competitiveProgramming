class Solution:
    def numberOfPairs(self, nums):
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        k = 0
        j = 0
        for el in d:
            k += d[el] // 2
            j += d[el] % 2
        return [k, j]


s = Solution()
print(s.numberOfPairs([1, 1, 2, 2]))
