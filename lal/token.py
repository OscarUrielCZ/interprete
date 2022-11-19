from enum import (auto, Enum, unique)
from typing import (NamedTuple, Dict)

@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    # DECLARATION = auto()
    DIVISION = auto()
    ELSE = auto()
    EOF = auto()
    EQ = auto()
    FALSE = auto()
    GT = auto()
    IDENTIFIER = auto()
    IF = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LET = auto()
    LPAREN = auto()
    LT = auto()
    MINUS = auto()
    MULTIPLICATION = auto()
    NEGATION = auto()
    NOT_EQ = auto()
    PLUS = auto()
    RBRACE = auto()
    RETURN = auto()
    RPAREN = auto()
    SEMICOLON = auto()
    TRUE = auto()
    VOID = auto()

class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}. Literal: {self.literal}'

def lookup_token_type(value: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'else': TokenType.ELSE,
        'false': TokenType.FALSE,
        'if': TokenType.IF,
        'int': TokenType.LET,
        'return': TokenType.RETURN,
        'true': TokenType.TRUE,
        'void': TokenType.VOID
    }

    return keywords.get(value, TokenType.IDENTIFIER)
