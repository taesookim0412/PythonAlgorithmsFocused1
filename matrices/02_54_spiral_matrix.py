from typing import List


class Solution:
    # seen matrix and direction list
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        seen = [[False for _ in range(len(row))] for row in matrix]
        x_moves = [1, 0, -1, 0]
        y_moves = [0, 1, 0, -1]
        direction = 0
        m, n = len(matrix), len(matrix[0])
        i, j, z = 0, 0, 0
        while z < m * n:
            res.append(matrix[i][j])
            seen[i][j] = True
            i += y_moves[direction]
            j += x_moves[direction]
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or seen[i][j]:
                i -= y_moves[direction]
                j -= x_moves[direction]
                direction = (direction + 1) % 4
                i += y_moves[direction]
                j += x_moves[direction]
            z += 1
        return res
# inorder
# def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#     if not matrix: return []
#     res = []
#     z, m, n = 0, len(matrix[0]), len(matrix)
#     top, right, bottom, left = 0, len(matrix[0]), len(matrix), 0
#     i = j = 0
#     while z < m * n:
#         for _ in range(left, right):
#             res.append(matrix[i][j])
#             j += 1
#         j -= 1
#         i += 1
#         top += 1
#         for _ in range(top, bottom):
#             res.append(matrix[i][j])
#             i += 1
#             print(i,j)
#         i -= 1
#         j -= 1
#         right -= 1
#         for _ in range(left, right):
#             res.append(matrix[i][j])
#             j -= 1
#         j += 1
#         i -= 1
#         bottom -= 1
#         for _ in range(top, bottom):
#             res.append(matrix[i][j])
#             i -= 1
#         i += 1
#         j += 1
#         left += 1
#         z += 1
#     return res



