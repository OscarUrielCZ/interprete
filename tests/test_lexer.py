from unittest import TestCase
from typing import List

from lal.token import (Token, TokenType)
from lal.lexer import Lexer

class LexerTest(TestCase):
    def test_ilegal(self) -> None:
        source: str = '¿¡@'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []

        for _ in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '¿'),
            Token(TokenType.ILLEGAL, '¡'),
            Token(TokenType.ILLEGAL, '@')
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_operators(self) -> None:
        source: str = '+='
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []

        for _ in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.ASSIGN, '=')
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_eof(self) -> None:
        source: str = '='
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []

        for _ in range(len(source)+1):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.EOF, '')
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_delimiters(self) -> None:
        source: str = '(){},;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []

        for _ in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens = [
            Token(TokenType.LPAREN, '('),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.SEMICOLON, ';')
        ]

        self.assertEqual(tokens, expected_tokens)
