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

    def test_assingment(self) -> None:
        source: str = 'int value = 4;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []

        for _ in range(5):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LET_INT, 'int'),
            Token(TokenType.IDENTIFIER, 'value'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '4'),
            Token(TokenType.SEMICOLON, ';')
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_procedure_declaration(self) -> None:
        source: str = '''
            void add(int x, int y) {
                x+y;
            }
        '''
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []

        for _ in range(15):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.VOID, 'void'),
            Token(TokenType.IDENTIFIER, 'add'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.LET_INT, 'int'),
            Token(TokenType.IDENTIFIER, 'x'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.LET_INT, 'int'),
            Token(TokenType.IDENTIFIER, 'y'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.IDENTIFIER, 'x'),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.IDENTIFIER, 'y'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}')
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_procedure_call(self) -> None:
        source: str = '     add(x, y);'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []

        for _ in range(7):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.IDENTIFIER, 'add'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENTIFIER, 'x'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENTIFIER, 'y'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.SEMICOLON, ';')
        ]

        self.assertEqual(tokens, expected_tokens)
