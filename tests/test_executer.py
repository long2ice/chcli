import pytest

from chcli.executer import get_columns, get_databases, get_server_info, get_tables


@pytest.mark.asyncio
async def test_get_server_info():
    ret = await get_server_info()
    assert isinstance(ret, list)


@pytest.mark.asyncio
async def test_get_databases():
    ret = await get_databases()
    assert "test" in ret


@pytest.mark.asyncio
async def test_get_tables():
    ret = await get_tables("chcli")
    assert ret == ["test"]


@pytest.mark.asyncio
async def test_get_columns():
    ret = await get_columns("chcli")
    assert ret == ["id", "decimal", "date", "datetime", "float", "uuid", "string", "ipv4", "ipv6"]
