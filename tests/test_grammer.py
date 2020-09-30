from antlr4 import CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import InputMismatchException
from antlr4.Token import CommonToken

from chcli.grammar.ClickHouseLexer import ClickHouseLexer
from chcli.grammar.ClickHouseParser import ClickHouseParser, InputStream


class SyntaxErrorListener(ErrorListener):
    def syntaxError(
        self,
        recognizer: ClickHouseParser,
        offendingSymbol: CommonToken,
        line: int,
        column: int,
        msg: str,
        e: InputMismatchException,
    ):
        if not e:
            return
        tokens = recognizer.getExpectedTokensWithinCurrentRule()
        words = []
        for i in tokens.intervals:
            for j in i:
                token = tokens.elementName(recognizer.literalNames, recognizer.symbolicNames, j)
                if token != "UNEXPECTED_CHAR":
                    words.append(token)
        print(words)


def test_select():
    sql = "select "
    lexer = ClickHouseLexer(InputStream(sql))
    stream = CommonTokenStream(lexer)
    parser = ClickHouseParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(SyntaxErrorListener())
    parser.parse()
