from typing import List, Optional

from async_lru import alru_cache

from chcli.connection import Connection


@alru_cache()
async def get_server_info():
    sql = "select * from system.build_options"
    ret = await Connection.execute(sql)
    return ret


@alru_cache()
async def show_tables(database: str) -> List[str]:
    sql = "show tables"
    ret = await Connection.execute(sql)
    return list(map(lambda x: x.get("name"), ret))


@alru_cache()
async def show_databases() -> List[str]:
    sql = "show databases"
    ret = await Connection.execute(sql)
    return list(map(lambda x: x.get("name"), ret))


@alru_cache()
async def get_columns(database: str, table: Optional[str] = None) -> List[str]:
    sql = f"""select name
from system.columns
where database = '{database}'"""
    if table:
        sql += f" and table={table}"
    ret = await Connection.execute(sql)
    return list(map(lambda x: x.get("name"), ret))
