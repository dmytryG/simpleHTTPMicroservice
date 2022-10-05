import asyncpg
from asyncpg import Record

from DB.BasicDAO import BasicDAO
from Models.User import User
from config import DB_PASSWORD, DB_USER, DB_NAME, DB_HOST


class PGDB(BasicDAO):

    def __init__(self):
        self.__connection: asyncpg.connection.Connection = None

    @staticmethod
    async def get_instance():
        if BasicDAO._instance is None:
            BasicDAO._instance = PGDB()
            BasicDAO._instance.__connection = await asyncpg.connect(user=DB_USER, password=DB_PASSWORD,
                                                                    database=DB_NAME, host=DB_HOST)

        if BasicDAO._instance.__connection.is_closed() or BasicDAO._instance.__connection is None:
            raise Exception("Can not connect to DB")

        return BasicDAO._instance

    async def add_user(self, user: User):
        try:
            await self.__connection.execute(
                "INSERT INTO \"Users\" (user_name, user_password) VALUES ($1, $2)",
                user.name,
                user.password)
        except asyncpg.exceptions.UniqueViolationError:
            raise Exception("User already registered")

    async def retrieve_user(self, user_name) -> User:
        result: list[Record] = await self.__connection.fetch(
            "SELECT * FROM \"Users\" WHERE user_name = $1;",
            user_name)

        if len(result) < 1:
            raise Exception("User not found")

        return User(result[0].get("user_name"), result[0].get("user_password"))

    async def login(self, user: User) -> bool:
        retrieved_user = await self.retrieve_user(user.name)

        return retrieved_user.password == user.password

    async def get_all_users(self) -> list[User]:
        result = await self.__connection.fetch(
            "SELECT * FROM \"Users\";")

        result = list(map(lambda user: User(user.get("user_name"), user.get("user_password")), result))

        return result
