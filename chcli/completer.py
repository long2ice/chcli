from typing import Iterable, List

from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document

from chcli import constants


class SqlCompleter(Completer):
    keywords: List[str] = [
        "SELECT",
        "INSERT",
        "INSERT INTO",
        "FROM",
        "CREATE",
        "CREATE TABLE",
        "WHERE",
        "JOIN",
        "ON",
        "DROP",
        "USE",
        "TABLE",
        "TABLES",
        "DATABASE",
        "INTO",
        "VALUES",
        "ALTER TABLE",
        "AS",
        "LIMIT",
        "GROUP BY",
        "UNION",
        "COLUMN",
        "IN",
        "IS",
    ]
    functions: List[str] = []
    types: List[str] = []
    _upper_mode = True

    @property
    def words(self):
        return set(self.keywords + self.functions + self.types)

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        word_before_cursor = document.get_word_before_cursor()
        text = document.text
        if not text.isupper():
            self._upper_mode = False
        else:
            self._upper_mode = True
        for word in self.words:
            if word_before_cursor.upper() in word:
                if self._upper_mode:
                    text = word.upper()
                else:
                    text = word.lower()
                yield Completion(text, start_position=-len(word_before_cursor))
        else:
            if document.text in constants.EXIT:
                yield Completion(constants.EXIT, start_position=-len(word_before_cursor))
