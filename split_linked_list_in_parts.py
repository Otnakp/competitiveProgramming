 #Definition for singly-linked list.

from typing import Optional, List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = self.calculate_len(head)
        result = [[] for _ in range(l)]
        p = l // k  # p per list
        r = l % k  # also add 1 extra from the start
        print(p)
        print(r)
        j = 0
        a = 0
        while head is not None:
            m = p + 1 if r >= 0 else p
            if a >= m:
                r -= 1
                a = 1
                j += 1
            else:
                a += 1

            result[j].append(head.val)
            head = head.next

        return result
    def calculate_len(self, head):
        l = 0
        while head is not None:
            l += 1
            head = head.next
        return l

s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(s.calculate_len(head))
result = s.splitListToParts(head, 3)
print(result)
