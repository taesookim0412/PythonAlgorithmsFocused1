from typing import List

#Runtime: O(n * a) where a = number of neighbors
#Memory: O(1)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False
        self.board = board
        self.word = word
        self.backtrack(0, 0, len(board), 0, len(board[0]))
        return self.res

    def backtrack(self, word_letter_idx, board_start_i, board_end_i, board_start_j, board_end_j):
        if word_letter_idx == len(self.word):
            self.res = True
            return
        start_i = max(0, board_start_i)
        end_i = min(len(self.board), board_end_i + 1)
        start_j = max(0, board_start_j)
        end_j = min(len(self.board[-1]), board_end_j + 1)
        for i in range(start_i, end_i):
            for j in range(start_j, end_j):
                if self.board[i][j] == self.word[word_letter_idx]:
                    if self.res is False:
                        temp = self.board[i][j]
                        self.board[i][j] = "_"
                        self.backtrack(word_letter_idx + 1, i - 1, i + 1, j, j)
                        self.backtrack(word_letter_idx + 1, i, i, j - 1, j + 1)
                        self.board[i][j] = temp


