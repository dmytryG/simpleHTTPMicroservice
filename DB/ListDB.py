from DB.BasicDAO import BasicDAO
from Models.User import User


class ListDB(BasicDAO):

    users = []

    async def add_user(self, user: User) -> None:
        for local_user in self.users:
            if local_user.name == user.name:
                raise Exception("User already registered")
        self.users.append(user)

    def retrieve_user(self, user_name) -> User:
        for local_user in self.users:
            if local_user.name == user_name:
                return local_user
        raise Exception("User not found")

    def login(self,  user: User) -> bool:
        for local_user in self.users:
            if local_user.name == user.name:
                if local_user.password == user.password:
                    return True
                else:
                    raise Exception("Incorrect password")

        raise Exception("User not found")