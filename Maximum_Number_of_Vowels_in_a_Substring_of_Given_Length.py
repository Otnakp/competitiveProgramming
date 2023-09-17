class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_len = 0
        i = 0
        vowels = {'a': True, 'e':True, 'i':True, 'o':True, 'u':True}
        while i < k:
            if s[i] in vowels:
                max_len += 1
            i += 1
        if max_len >= k:
            return k
        m = max_len
        while i < len(s):
            if s[i - k] not in vowels and s[i] in vowels:
                max_len += 1
            elif s[i - k] in vowels and s[i] not in vowels:
                max_len -= 1 if max_len >= 1 else 0
            if max_len == k:
                return k
            m = max(max_len, m)
            i += 1
        return m

s = Solution()
print(s.maxVowels("leetcode", 3))
"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

optimized version. in the sliding window technique if you put both ifs like this it automatically
removes the need to check all possible combinations of things because you may gain 1 if there is a voewl
but if you lost a vowel you just remove 1 later, this removes all those longs ifs that are inefficient
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_count = count = sum(1 for c in s[:k] if c in vowels)
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            max_count = max(max_count, count)
        
        return max_count
"""