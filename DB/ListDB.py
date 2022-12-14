from DB.BasicDAO import BasicDAO
from Models.User import User


class ListDB(BasicDAO):
    __users = []

    @staticmethod
    async def get_instance():
        if BasicDAO._instance is None:
            BasicDAO._instance = ListDB()
        return BasicDAO._instance

    async def add_user(self, user: User):
        for local_user in self.__users:
            if local_user.name == user.name:
                raise Exception("User already registered")
        self.__users.append(user)

    async def retrieve_user(self, user_name) -> User:
        for local_user in self.__users:
            if local_user.name == user_name:
                return local_user
        raise Exception("User not found")

    async def login(self, user: User) -> bool:
        for local_user in self.__users:
            if local_user.name == user.name:
                if local_user.password == user.password:
                    return True
                else:
                    raise Exception("Incorrect password")

        raise Exception("User not found")

    async def get_all_users(self) -> list[User]:
        return self.__users
