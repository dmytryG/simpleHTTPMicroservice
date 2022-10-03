from abc import abstractmethod, ABCMeta

from Models.User import User


class BasicDAO():
    __metaclass__ = ABCMeta

    @abstractmethod
    async def add_user(self,  user: User) -> None:
        """Add user to database (register)"""

    @abstractmethod
    async def retrieve_user(self, user_name) -> User:
        """Gets user data"""

    @abstractmethod
    async def login(self,  user: User) -> bool:
        """Checking if user_name exists and password is correct"""
