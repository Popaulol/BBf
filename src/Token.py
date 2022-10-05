from enum import Enum, auto


class TokenType(Enum):
    left_angle_brace = auto()  # <
    right_angle_brace = auto()  # >
    plus = auto()  # +
    minus = auto()  # -
    dot = auto()  # .
    comma = auto()  # ,
    left_square_bracket = auto()  # [
    right_square_bracket = auto()  # ]

    hash_symbol = auto()  # #

    A = auto()  # A
    B = auto()  # B
    C = auto()  # C
    D = auto()  # D
    E = auto()  # E
    F = auto()  # F
    G = auto()  # G

    a = auto()  # a
    b = auto()  # b
    c = auto()  # c
    d = auto()  # d
    e = auto()  # e
    f = auto()  # f
    g = auto()  # g

    pipe = auto()  # |
    caret = auto()  # ^
    left_paran = auto()  # (
    right_paran = auto()  # )
    left_curly = auto()  # {
    right_curly = auto()  # }
    bang = auto()  # !
    question = auto()  # ?
    percent = auto()  # %
    ampersand = auto()  # &
    paragraph = auto()  # §

    comment = auto()
