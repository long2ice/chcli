import asyncio

import pytest

from chcli.connection import Connection


@pytest.yield_fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    res = policy.new_event_loop()
    asyncio.set_event_loop(res)
    res._close = res.close
    res.close = lambda: None

    yield res

    res._close()


@pytest.fixture(scope="session", autouse=True)
async def initialize_tests():
    await Connection.connect_server(database="chcli")
    await Connection.execute("create database if not exists chcli")
    await Connection.execute(
        """CREATE TABLE if not exists chcli.test
    (
        `id`       Int32,
        `decimal`  Decimal(10, 2),
        `date`     Date,
        `datetime` DateTime,
        `float`    Float32,
        `uuid`     UUID,
        `string`   String,
        `ipv4`     IPv4,
        `ipv6`     IPv6

    )
        ENGINE = MergeTree
            ORDER BY id"""
    )
