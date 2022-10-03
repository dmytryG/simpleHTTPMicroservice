from DB.BasicDAO import BasicDAO
from Models.User import User


class ListDB(BasicDAO):

    users = []

    @staticmethod
    def get_instance():
        if ListDB.instance is None:
            ListDB.instance = ListDB()
        return ListDB.instance

    async def add_user(self, user: User) -> None:
        for local_user in self.users:
            if local_user.name == user.name:
                raise Exception("User already registered")
        self.users.append(user)

    async def retrieve_user(self, user_name) -> User:
        for local_user in self.users:
            if local_user.name == user_name:
                return local_user
        raise Exception("User not found")

    async def login(self,  user: User) -> bool:
        for local_user in self.users:
            if local_user.name == user.name:
                if local_user.password == user.password:
                    return True
                else:
                    raise Exception("Incorrect password")

        raise Exception("User not found")

    async def getAllUsers(self, user: User) -> list[User]:
        return self.users

