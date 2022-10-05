from abc import abstractmethod, ABCMeta

from Models.User import User


class BasicDAO:
    __metaclass__ = ABCMeta

    _instance = None

    @staticmethod
    async def get_instance():
        if BasicDAO._instance is None:
            raise Exception("You have to initialize and datasource before call get_instance()")
        else:
            return BasicDAO._instance

    @abstractmethod
    async def add_user(self, user: User):
        """Add user to database (register)"""

    @abstractmethod
    async def retrieve_user(self, user_name) -> User:
        """Gets user data"""

    @abstractmethod
    async def login(self, user: User) -> bool:
        """Checking if user_name exists and password is correct"""

    @abstractmethod
    async def get_all_users(self) -> list[User]:
        """Returning all the users"""
