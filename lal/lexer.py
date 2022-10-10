from re import match

from lal.token import (Token, TokenType, lookup_token_type)

class Lexer:
    def __init__(self, source) -> None:
        self._source: str = source
        self._char: str = ''
        self._pos: int = 0

    def next_token(self) -> Token:
        self._read_char()
        self._skip_whitespace()

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
        elif self._is_letter(self._char):
            literal: str = self._read_string()
            token_type: TokenType = lookup_token_type(literal)
            token = Token(token_type, literal)
        elif self._is_number(self._char):
            number: str = self._read_number()
            token = Token(TokenType.INT, number)
        else:
            token = Token(TokenType.ILLEGAL, self._char)

        return token

    def _is_letter(self, char: str) -> bool:
        return bool(match(r'^[a-zA-Z_]$', char))

    def _is_number(self, char: str) -> bool:
        return bool(match(r'^\d$', char))

    def _skip_whitespace(self) -> None:
        while match('^\s$', self._char):
            self._read_char()

    def _read_char(self) -> None:
        if self._pos >= len(self._source):
            self._char = ''
        else:
            self._char = self._source[self._pos]
            self._pos += 1

    def _rollback_pos(self) -> None:
        self._pos -= 1

    def _read_string(self) -> str:
        initial_pos: int = self._pos-1
        while self._is_letter(self._char):
            self._read_char()
        self._rollback_pos()
        return self._source[initial_pos:self._pos]

    def _read_number(self) -> str:
        initial_pos: int = self._pos-1
        while self._is_number(self._char):
            self._read_char()
        self._rollback_pos()
        return self._source[initial_pos:self._pos]
