import re
from typing import AsyncGenerator, Iterable, List

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import InputMismatchException
from antlr4.Token import CommonToken
from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document

from chcli import constants
from chcli.connection import Connection
from chcli.executer import get_columns, get_databases, get_tables
from chcli.grammar.ClickHouseLexer import ClickHouseLexer
from chcli.grammar.ClickHouseParser import ClickHouseParser


class SyntaxErrorListener(ErrorListener):
    def __init__(self, completer: "SqlCompleter"):
        self.completer = completer

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
        tokens = e.getExpectedTokens()
        words = []
        for i in tokens.intervals:
            for j in i:
                token = tokens.elementName(recognizer.literalNames, recognizer.symbolicNames, j)
                if token != "UNEXPECTED_CHAR":
                    words.append(token.replace("K_", "").replace("'", ""))
        self.completer.set_words(words)


class SqlCompleter(Completer):
    _upper_mode = True
    _words: List[str] = []
    _database = "database"
    _table = "table"
    _column = "column"

    def set_words(self, words: List[str]):
        self._words = words

    def parse(self, text: str):
        lexer = ClickHouseLexer(InputStream(text))
        stream = CommonTokenStream(lexer)
        parser = ClickHouseParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(SyntaxErrorListener(self))
        parser.parse()

    def _get_last_word(self, text: str) -> str:
        if not text:
            return ""
        regex = re.compile(r"(\w+)")
        matches = regex.findall(text)
        if matches:
            if text[-1].isspace():
                return matches[-1]
            if len(matches) > 1:
                return matches[-2]
            return matches[-1]
        else:
            return ""

    def _get_suggest_type(self, word: str):
        return {
            constants.USE: self._database,
            constants.FROM: self._table,
            constants.INSERT: self._table,
            constants.TABLE: self._table,
            constants.INTO: self._table,
            constants.SELECT: self._column,
            constants.WHERE: self._column,
        }.get(word.upper())

    async def suggest_by_last_word(self, text: str):
        last_word = self._get_last_word(text).upper()
        type_ = self._get_suggest_type(last_word)
        if type_ == self._database:
            databases = await get_databases()
            self._words = databases
            return True
        elif type_ == self._table:
            tables = await get_tables(Connection.database)
            self._words = tables
            return True
        elif type_ == self._column:
            columns = await get_columns(Connection.database)
            self._words = columns
            return True
        return False

    async def get_completions_async(
        self, document: Document, complete_event: CompleteEvent
    ) -> AsyncGenerator[Completion, None]:
        word_before_cursor = document.get_word_before_cursor()
        text = document.text
        if not await self.suggest_by_last_word(text):
            self.parse(text)

        if not text.isupper():
            self._upper_mode = False
        else:
            self._upper_mode = True
        for word in self._words:
            if word_before_cursor.upper() in word or word_before_cursor.lower() in word:
                if self._upper_mode:
                    w = word.upper()
                else:
                    w = word.lower()
                yield Completion(w, start_position=-len(word_before_cursor))
        else:
            if document.text in constants.EXIT:
                yield Completion(constants.EXIT, start_position=-len(word_before_cursor))

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        pass
