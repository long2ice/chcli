from typing import Dict, List

from asynch.errors import ServerException
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.sql import SqlLexer
from rich.console import Console

from chcli.connection import Connection

from . import __version__
from .completion import ClickHouseCompleter

console = Console(highlight=False)
completer = ClickHouseCompleter()
session = PromptSession(
    completer=completer, auto_suggest=AutoSuggestFromHistory(), lexer=PygmentsLexer(SqlLexer)
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


async def run():
    text = ""
    while text != "exit":
        try:
            text = await session.prompt_async()
            if text != "exit":
                try:
                    ret = await Connection.execute(text)
                    console.print(ret)
                except ServerException as e:
                    console.print(e, style="bold red")
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
    console.print("GoodBye!")
