from unittest import TestCase
from typing import (Any, cast, List, Type)

from lal.ast import (
    Expression,
    ExpressionStatement,
    Identifier,
    LetStatement, 
    Program, 
    ReturnStatement
)
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

        self.assertEqual(len(program.statements), 3)

        for statement in program.statements:
            self.assertEqual(statement.token_literal(), "int")
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

        self.assertEqual(names, expected_names)

    def test_unexpected_tokens(self) -> None:
        source: str = "int a 5;"

        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program = parser.parse_program()

        self.assertEqual(len(parser.errors), 1)

    def test_parse_return_statements(self) -> None:
        source: str = """
            return 10;
            return foo;
        """

        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self.assertEqual(len(program.statements), 2)

        for statement in program.statements:
            self.assertEqual(statement.token_literal(), "return")
            self.assertIsInstance(statement, ReturnStatement)

    def test_identifier_expression(self) -> None:
        source: str = "foobar;"
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program = parser.parse_program()
        self._test_program_statements(parser, program)

        expression_statement = cast(ExpressionStatement, program.statements[0])
        assert expression_statement.expression is not None
        self._test_literal_expression(expression_statement.expression, "foobar")

    def _test_program_statements(self,
                                parser: Parser,
                                program: Program,
                                expected_statements_count: int = 1) -> None:
        self.assertEqual(len(parser.errors), 0)
        self.assertEqual(len(program.statements), expected_statements_count)
        self.assertIsInstance(program.statements[0], ExpressionStatement)

    def _test_literal_expression(self,
                                expression: Expression,
                                expected_value: Any) -> None:
        
        value_type: Type = type(expected_value)

        if value_type == str:
            self._test_identifier(expression, expected_value)
        else:
            self.fail(f"Unhandled type of expression. Got={value_type}")

    def _test_identifier(self,
                        expression: Expression,
                        expected_value: str) -> None:
        self.assertIsInstance(expression, Identifier)
        identifier = cast(Identifier, expression)
        self.assertEqual(identifier.value, expected_value)
        self.assertEqual(identifier.token_literal(), expected_value)