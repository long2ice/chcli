import asyncio
import sys
from functools import wraps

import click
from asynch.errors import ServerException

from chcli import __version__, console
from chcli.common import init
from chcli.connection import Connection


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@click.command(help="A Terminal Client for ClickHouse with AutoCompletion and Syntax Highlighting.")
@click.version_option(__version__, "-v", "--version")
@click.option(
    "-h", "--host", default="127.0.0.1", show_default=True, help="ClickHouse server host.",
)
@click.option(
    "-p", "--port", default=9000, type=int, show_default=True, help="ClickHouse server port.",
)
@click.option(
    "-u", "--user", default="default", show_default=True, help="ClickHouse server user.",
)
@click.password_option(
    confirmation_prompt=False, show_default=False, default="", help="ClickHouse server password.",
)
@coro
async def cli(host: str, port: int, user: str, password: str):
    try:
        await Connection.connect_server(host, port, user=user, password=password)
        await init()
        await console.run()
    except ServerException as e:
        console.console.print(e, style="bold red")


def main():
    sys.path.insert(0, ".")
    cli()


if __name__ == "__main__":
    main()
