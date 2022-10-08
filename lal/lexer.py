from re import match

from lal.token import (Token, TokenType)

class Lexer:
    def __init__(self, source) -> None:
        self._source: str = source
        self._char: str = ''
        self._pos: int = 0

    def next_token(self) -> Token:
        self._read_char()

        if match(r'^=$', self._char):
            token = Token(TokenType.ASSIGN, self._char)
        elif match(r'^\+$', self._char):
            token = Token(TokenType.PLUS, self._char)
        elif match(r'^$', self._char):
            token = Token(TokenType.EOF, self._char)
        elif match(r'^\($', self._char):
            token = Token(TokenType.LPAREN, self._char)
        elif match(r'^\)$', self._char):
            token = Token(TokenType.RPAREN, self._char)
        elif match(r'^\{$', self._char):
            token = Token(TokenType.LBRACE, self._char)
        elif match(r'^\}$', self._char):
            token = Token(TokenType.RBRACE, self._char)
        elif match(r'^,$', self._char):
            token = Token(TokenType.COMMA, self._char)
        elif match(r'^;$', self._char):
            token = Token(TokenType.SEMICOLON, self._char)
        else:
            token = Token(TokenType.ILLEGAL, self._char)

        return token

    def _read_char(self) -> None:
        if self._pos >= len(self._source):
            self._char = ''
        else:
            self._char = self._source[self._pos]
            self._pos += 1
