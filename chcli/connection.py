from asynch import connect
from asynch.cursors import DictCursor


class Connection:
    _conn = None
    host = None
    port = None
    user = None
    password = None
    database = None
    prompt_session = None

    @classmethod
    async def connect_server(
        cls,
        host: str = "127.0.0.1",
        port: int = 9000,
        database: str = "default",
        user: str = "default",
        password: str = "",
    ):
        cls.host = host
        cls.port = port
        cls.user = user
        cls.password = password
        cls.database = database
        if cls._conn:
            return cls._conn
        cls._conn = await connect(
            host=host, port=port, database=database, user=user, password=password,
        )

    @classmethod
    async def get_conn(cls):
        if not cls._conn:
            raise ValueError("Should call connect_server first!")
        return cls._conn

    @classmethod
    async def execute(cls, query: str):
        conn = await cls.get_conn()
        async with conn.cursor(cursor=DictCursor) as cursor:
            await cursor.execute(query)
            ret = cursor.fetchall()
            db = cls._is_use_database(query)
            if db:
                cls.database = db
                cls.refresh_prompt_message()
            if ret:
                return ret

    @classmethod
    def _is_use_database(cls, query: str):
        if query.startswith(("use", "USE")):
            return query.split(" ")[1].strip()

    @classmethod
    def refresh_prompt_message(cls):
        if cls.database == "default":
            cls.prompt_session.message = (
                f"\n{Connection.user}@{Connection.host}:{Connection.port}:({Connection.database})> "
            )
        else:
            cls.prompt_session.message = (
                f"\n{Connection.user}@{Connection.host}:{Connection.port}:{Connection.database}> "
            )
