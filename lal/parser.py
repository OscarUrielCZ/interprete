from typing import Optional

from lal.ast import (Program, Statement)
from lal.lexer import Lexer
from lal.token import (Token, TokenType)

class Parser:
    def __init__(self, lexer: Lexer) -> None:
        self._lexer = lexe
        self._current_token: Optional[Token] = None
        self._peek_token: Optional[Token] = None

    def parse_program(self) -> Program:
        program: Program = Program(statements=[])

        assert self._current_token is not None

        while self._current_token.token_type != TokenType.EOF:
            statement = self._parse_statement()
            if statement is not None:
                program.statements.append(statement)

        return program

    def _parse_let_statement(self) -> Optional[LetStatement]:
        assert self._current_token is not None
        let_statement = LetStatement(token=self._current_token)

        if not self._expected_token(TokenType.IDENTIFIER):
            return None

        let_statement.name =  Identifier(token=self.current_token, value=self.current_token.literal)

        if not self._expected_token(TokenType.ASSIGN):
            return None

        # TODO terminar cuando sepamos parsar expresiones

    def _parse_statement(self) -> Optional[Statement]:
        assert self._current_token is not None
        if self._current_token.token_type = TokenType.LET_INT
            return self._parse_let_statement()
        else:
            return None
