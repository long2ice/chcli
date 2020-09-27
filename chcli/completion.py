from typing import Iterable, List

from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document


class ClickHouseCompleter(Completer):
    keywords: List[str] = ["SELECT", "FROM", "WHERE", "JOIN", "ON"]
    functions: List[str] = []

    def _get_all_words(self):
        return set(self.keywords + self.functions)

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        text = document.text
        for item in self._get_all_words():
            if item.startswith(text.upper()):
                yield Completion(item, start_position=0)
