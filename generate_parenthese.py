from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return rec_parentheses(n, 0)


def rec_parentheses(left, right, t_str="", result=None):
    if result is None:
        result = []

    if left == 0 and right == 0:
        result.append(t_str)

    if left > 0:
        rec_parentheses(left - 1, right + 1, t_str + "(", result)
    if right > 0:
        rec_parentheses(left, right - 1, t_str + ")", result)

    return result


s = Solution()
print(s.generateParenthesis(3))
