from unittest import TestCase
from typing import (cast, List)

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
            self.assertEquals(statement.token_literal(), "int")
            self.assertIsInstance(statement, LetStatement)

    def test_identifier_names(self) -> None:
        source: str = """
            int foo = 10;
            int eg = 222;
            int dog = 4;
        """

        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program = parser.parse_program()

        names: List[str] = []

        for statement in program.statements:
            let_statement = cast(LetStatement, statement)
            assert let_statement.name is not None
            names.append(let_statement.name.value)

        expected_names: List[str] = ["foo", "eg", "dog"]

        self.assertEquals(names, expected_names)

    def test_unexpected_tokens(self) -> None:
        source: str = "int a 5;"

        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program = parser.parse_program()

        self.assertEquals(len(parser.errors), 1)