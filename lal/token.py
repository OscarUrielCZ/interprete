from enum import (auto, Enum, unique)
from typing import (NamedTuple, Dict)

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
    LET_INT = auto()
    LPAREN = auto()
    PLUS = auto()
    RBRACE = auto()
    RPAREN = auto()
    SEMICOLON = auto()
    VOID = auto()

class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}. Literal: {self.literal}'

def lookup_token_type(value: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'int': TokenType.LET_INT,
        'void': TokenType.VOID
    }

    return keywords.get(value, TokenType.IDENTIFIER)
