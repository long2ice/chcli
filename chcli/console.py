import time
from typing import Any, Dict, List

from asynch.errors import ServerException
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.sql import SqlLexer
from rich.console import Console, RichCast
from rich.table import Table

from chcli.connection import Connection

from . import __version__, constants
from .completer import SqlCompleter
from .key_bindings import kb

console = Console(highlight=False)
completer = SqlCompleter()
session = PromptSession(
    completer=completer,
    auto_suggest=AutoSuggestFromHistory(),
    lexer=PygmentsLexer(SqlLexer),
    key_bindings=kb,
)


def server_info(info: List[Dict]):
    """
    print server info
    """
    version = reversion = ""
    for item in info:
        name = item.get("name")
        value = item.get("value")
        if name == "VERSION_DESCRIBE":
            version = value
        elif name == "VERSION_REVISION":
            reversion = value
    console.print(f"Connecting to {Connection.host}:{Connection.port} as user {Connection.user}.")
    console.print(f"Connected to ClickHouse server version {version} revision {reversion}.\n")


def cli_info():
    console.print(f"chcli {__version__}")
    console.print("author: long2ice")
    console.print("github: https://github.com/long2ice/chcli")


class RenderAble(RichCast):
    def __init__(self, value: Any):
        self.value = str(value)

    def __rich__(self):
        return self.value


async def run():
    text = ""
    while text != constants.EXIT:
        try:
            text = await session.prompt_async()
            text = text.strip()
            if text != constants.EXIT:
                try:
                    start = time.time()
                    ret = await Connection.execute(text)
                    if ret:
                        pretty_table(ret)
                    end = time.time()
                    ms = int((end - start) * 1000)
                    console.print(f"\ncomplete in {ms} ms")
                except ServerException as e:
                    console.print(e, style="bold red")
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
    console.print("GoodBye!")


def pretty_table(data: List[Dict]):
    table = Table(show_header=True, header_style="bold magenta")
    for k in data[0].keys():
        table.add_column(k)
    for item in data:
        table.add_row(*map(lambda x: RenderAble(x), item.values()))
    console.print(table)