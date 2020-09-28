from chcli.connection import Connection


async def get_server_info():
    sql = "select * from system.build_options"
    ret = await Connection.execute(sql)
    return ret
