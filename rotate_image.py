from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(f"{i}, {j}")


s = Solution()
s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
