import lexer
import parse

def main():
    content = ""
    with open("test.bart","r") as file:
        content = file.read()

        lex = lexer.Lexer(content)
        tokens = lex.tokenize()

        pars = parse.Parser(tokens)
        pars.parse()
main()