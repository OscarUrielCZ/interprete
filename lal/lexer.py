from re import match

from lal.token import (Token, TokenType, lookup_token_type)

class Lexer:
    def __init__(self, source) -> None:
        self._source: str = source
        self._char: str = ''
        self._pos: int = 0
        self._read_pos: int = 0

    def next_token(self) -> Token:
        self._read_char()
        self._skip_whitespace()

        if match(r'^=$', self._char):
            if self._peek_char() == '=':
                token = self._make_two_char_token(TokenType.EQ)
            else:
                token = Token(TokenType.ASSIGN, self._char)
        elif match(r'^\+$', self._char):
            token = Token(TokenType.PLUS, self._char)
        elif match(r'^\-$', self._char):
            token = Token(TokenType.MINUS, self._char)
        elif match(r'^\*$', self._char):
            token = Token(TokenType.MULTIPLICATION, self._char)
        elif match(r'^/$', self._char):
            token = Token(TokenType.DIVISION, self._char)
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
        elif match(r'^<$', self._char):
            token = Token(TokenType.LT, self._char)
        elif match(r'^>$', self._char):
            token = Token(TokenType.GT, self._char)
        elif match(r'^!$', self._char):
            if self._peek_char() == '=':
                token = self._make_two_char_token(TokenType.NOT_EQ)
            else:
                token = Token(TokenType.NEGATION, self._char)
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

    def _make_two_char_token(self, token_type: TokenType) -> Token:
        prefix = self._char
        self._read_char()
        sufix= self._char

        return Token(token_type, prefix+sufix)

    def _peek_char(self) -> str:
        if self._read_pos >= len(self._source):
            return ''
        return self._source[self._read_pos]

    def _read_char(self) -> None:
        if self._read_pos >= len(self._source):
            self._char = ''
        else:
            self._char = self._source[self._read_pos]
            self._pos = self._read_pos
            self._read_pos += 1

    def _read_string(self) -> str:
        initial_pos: int = self._pos
        while self._is_letter(self._char) or self._is_number(self._char):
            self._read_char()
        final_pos: int = self._pos
        self._rollback_pos()
        return self._source[initial_pos:final_pos]

    def _read_number(self) -> str:
        initial_pos: int = self._pos
        while self._is_number(self._char):
            self._read_char()
        final_pos: int = self._pos
        self._rollback_pos()
        return self._source[initial_pos:final_pos]

    def _rollback_pos(self) -> None:
        self._read_pos = self._pos
        self._pos -= 1

    def _skip_whitespace(self) -> None:
        while match('^\s$', self._char):
            self._read_char()

