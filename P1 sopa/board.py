from size import Size
from word import Word
import random
from utils import *


class Board:
    def __init__(self, size, words):
        self.size = size
        self.n = words
        self.words = []
        self.generate_board()

    def generate_board(self):
        self._create_board()
        self._fill_random_words()
        self._fill_random_letters()

    def _create_board(self):
        w, h = self.size
        self.board = [['.' for _ in range(h)] for _ in range(w)]

    def _generate_position(self):
        w, h = self.size
        px = random.randint(0, w)
        py = random.randint(0, h)
        return (px, py)

    def _generate_direction(self):
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)
        while dx == 0 and dy == 0:
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
        return (dx, dy)

    def _generate_range(self, position, direction):
        return get_pos(position, direction, self.board)

    def _generate_str(self, range_):
        board_str = ''
        for i, j in range_:
            board_str += self.board[i][j]
        return board_str

    def _insert_word(self, word, begin_idx, range_):
        for c, [i, j] in zip(word, range_[begin_idx:]):
            if self.board[i][j] != c and self.board[i][j] != '.':
                print('err')
            self.board[i][j] = c

    def _get_word_and_begin_idx(self, board_str, range_):
        board_str = self._generate_str(range_)

        full_regex = gen_regex_full(board_str)
        partial_regex = gen_regex_partial(board_str)

        full_regex_expr = gen_expr(full_regex)
        partial_regex_expr = gen_expr(partial_regex)

        new_word = Word.get_special(full_regex_expr, min(self.size))
        if not new_word:
            return None

        regex_word = partial_regex_expr(new_word)
        if not regex_word:
            return None
        span_word = regex_word.span()

        span_board_str = partial_regex_expr(new_word).span()

        begin_idx = span_board_str[0]-span_word[0]
        return (new_word, begin_idx)

    def _fill_random_words(self):
        while len(self.words) < self.n:
            position = self._generate_position()
            direction = self._generate_direction()

            range_ = self._generate_range(position, direction)

            board_str = self._generate_str(range_)

            word = self._get_word_and_begin_idx(board_str, range_)
            if not word:
                continue
            new_word, begin_idx = word
            self.words.append(new_word)
            self._insert_word(new_word, begin_idx, range_)

    def _fill_random_letters(self):
        letras = "ABCDEFGHIJLMNOPQRSTUVWXYZÑÁÉÍÓÚÜ"
        res = []
        for r in self.board:
            no_points = [c if c != '.' else random.choice(letras) for c in r]
            res.append(no_points)
        self.board = res


if __name__ == "__main__":
    board = Board(Size(15, 15), 20)
    print(board.words)
    for r in board.board:
        print(r)
