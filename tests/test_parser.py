from unittest import TestCase

from lal.ast import (Program, LetStatement)
from lal.lexer import Lexer
from lal.parser import Parser

class ParserTest(TestCase):
    def test_parse_program(self) -> None:
        source : str = "int num =10;"
        lexer : Lexer = Lexer(source)
        parser : Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self.assertIsNotNone(program)
        self.assertIsInstance(program, Program)

    def test_parse_let_statements(self) -> None:
        source: str = """
            int foo = 10;
            int eg = 222;
            int dog = 4;
        """

        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program = parser.parse_program()

        self.assertEquals(len(program.statements), 3)

        for statement in program.statements:
            self.assertEquals(statement.token_literal(), "variable")
            self.assertIsInstance(statement, LetStatement)
