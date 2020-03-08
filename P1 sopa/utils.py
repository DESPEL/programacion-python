import re
import random


def gen_regex_full(s):
    inside = False
    regex = ''
    for c in s:
        if c == '.' and not inside:
            regex += '.?'
        elif c == '.' and inside:
            regex += '.'
        else:
            regex += c
            inside = True
    delta = len(regex) - len(regex.rstrip('.'))
    regex = regex.rstrip('.') + '.?'*delta
    return '^' + regex + '$'


def gen_regex_partial(s):
    inside = False
    regex = ''
    for c in s:
        if c == '.' and inside:
            regex += '.'
        else:
            regex += c
            inside = True
    regex = regex.rstrip('.')
    return regex


def gen_expr(regex):
    return lambda x: re.match(regex, x)


def get_pos(pos, direction, board):
    x, y = pos
    dx, dy = direction

    index_list = []

    while x > 0 and x < len(board)-1 and y > 0 and y < len(board[0])-1:
        x -= dx
        y -= dy
    while x >= 0 and x <= len(board)-1 and y >= 0 and y <= len(board[0])-1:
        index_list.append([x, y])
        x += dx
        y += dy
    return index_list[0:12]


def get_board_str(board, range_):
    board_str = ''
    for i, j in range_:
        board_str += board[i][j]
    return board_str


def insert_word(board, word, begin_idx, range_):
    for c, [i, j] in zip(word, range_[begin_idx:]):
        if board[i][j] != c and board[i][j] != '.':
            print('err')
        board[i][j] = c
