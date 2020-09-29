from chcli import console
from chcli.connection import Connection
from chcli.console import session
from chcli.executer import get_server_info


async def init():
    server_info = await get_server_info()
    console.server_info(server_info)
    console.cli_info()
    Connection.prompt_session = session
    Connection.refresh_prompt_message()
