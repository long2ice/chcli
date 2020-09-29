import pytest

from chcli.executer import get_server_info, show_tables


@pytest.mark.asyncio
async def test_get_server_info():
    ret = await get_server_info()
    assert isinstance(ret, list)


@pytest.mark.asyncio
async def test_show_tables():
    ret = await show_tables("chcli")
    assert ret == ["test"]
