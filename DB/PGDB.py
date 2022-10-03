import asyncpg
from asyncpg import Record


from DB.BasicDAO import BasicDAO
from Models.User import User


class PGDB(BasicDAO):

    def __init__(self):
        self.connection = None

    @staticmethod
    async def get_instance():
        if PGDB.instance is None:
            PGDB.instance = PGDB()
            PGDB.instance.connection = await asyncpg.connect(user="postgres", password="postgres",
                                              database="basicHttpMicroservice", host="127.0.0.1")
        return PGDB.instance

    async def add_user(self, user: User) -> None:
        pass

    async def retrieve_user(self, user_name) -> User:
        pass

    async def login(self, user: User) -> bool:
        pass

    async def getAllUsers(self, user: User) -> list[User]:
        pass