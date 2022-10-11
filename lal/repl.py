from lal.lexer import Lexer
from lal.token import (Token, TokenType)

EOF_TOKEN : Token = Token(TokenType.EOF, '')

def start_repl() -> None:
    while (source := input('>> ')) != 'exit()':
        lexer : Lexer = Lexer(source)

        while (token := lexer.next_token()) != EOF_TOKEN:
            print(token)
