from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # passes
        # Try to reach any piece of the array that has a 0 in it
        # you may fail and then return false, you can move i + arr[i] and i - arr[i]
        frontier = [start]
        d = {}
        while len(frontier) > 0:
            t = frontier.pop()
            r = t + arr[t]
            l = t - arr[t]
            if r < len(arr) and r not in d:
                frontier.append(r)
                if t not in d:
                    d[t] = [None, arr[r]]
                else:
                    d[t][1] = arr[r]
            if l >= 0 and l not in d:
                frontier.append(l)
                if t not in d:
                    d[t] = [arr[l], None]
                else:
                    d[t][0] = arr[l]
        for k in d:
            if d[k][0] == 0 or d[k][1] == 0:
                return True
        return False

arr = [4,2,3,0,3,1,2]
start = 5
s = Solution()
print(s.canReach(arr, start))
# success
# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/
