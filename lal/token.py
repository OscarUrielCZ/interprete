from enum import (auto, Enum, unique)
from typing import NamedTuple

@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    DECLARATION = auto()
    EOF = auto()
    FUNCTION = auto()
    IDENTIFIER = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LPAREN = auto()
    PLUS = auto()
    RBRACE = auto()
    RPAREN = auto()
    SEMICOLON = auto()

class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}. Literal: {self.literal}'
