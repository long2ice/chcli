from typing import Iterable

from prompt_toolkit.completion import Completer, CompleteEvent, Completion
from prompt_toolkit.document import Document


class ClickHouseCompleter(Completer):
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]:
        pass
