from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False
        self.board = board
        self.word = word

        self.backtrack(0, 0, len(board), 0, len(board[0]))
        return self.res

    def backtrack(self, word_letter_idx, board_start_i, board_end_i, board_start_j, board_end_j):
        print(word_letter_idx)
        if word_letter_idx == len(self.word):
            self.res = True
            return
        for i in range(max(0, board_start_i), min(len(self.board), board_end_i)):
            for j in range(max(0, board_start_j), min(len(self.board[i]), board_end_j)):
                if self.board[i][j] == self.word[word_letter_idx]:
                    if not self.res:
                        self.backtrack(word_letter_idx + 1, i - 1, i + 1, j, j)
                        self.backtrack(word_letter_idx + 1, i, i, j - 1, j + 1)