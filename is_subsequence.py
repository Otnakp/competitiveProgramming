class Solution:
    def isSubsequence(self, s, t):
        i0 = 0
        i1 = 0
        while i0 < len(s) and i1 < len(t):
            if s[i0] == s[i1]:
                i0 += 1
                i1 += 1
            else:
                i1 += 1
        print(i0)
        if i0 == len(s):
            return True
        return False


s = Solution()
print(s.isSubsequence("abc", "addddbddddcdddd"))
