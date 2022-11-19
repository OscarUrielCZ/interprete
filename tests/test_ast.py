from unittest import TestCase

from lal.ast import (Identifier, LetStatement, Program, ReturnStatement)
from lal.token import (Token, TokenType)

class ASTTest(TestCase):

    def test_let_statement(self) -> None:
        program: Program = Program(statements=[
            LetStatement(
                token=Token(TokenType.LET, "int"),
                name=Identifier(token=Token(TokenType.IDENTIFIER, "my_var"), value="my_var"),
                value=Identifier(token=Token(TokenType.IDENTIFIER, "an_expression"), value="an_expression")
            )
        ])

        program_str = str(program)

        self.assertEqual(program_str, "int my_var = an_expression;")

    def test_return_statement(self) -> None:
        program: Program = Program(statements=[
            ReturnStatement(
                token=Token(TokenType.RETURN, "return"),
                return_value=Identifier(token=Token(TokenType.IDENTIFIER, "foo"), value="foo")
            )
        ])

        program_str = str(program)

        self.assertEqual(program_str, "return foo;")