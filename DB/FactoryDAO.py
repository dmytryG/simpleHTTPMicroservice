import sys

from config import DAO_CLASS

from DB.BasicDAO import BasicDAO
from DB.PGDB import PGDB
from DB.ListDB import ListDB


class FactoryDAO:

    @staticmethod
    async def get_instance():
        if BasicDAO.instance is None:
            await getattr(sys.modules[__name__], DAO_CLASS).get_instance()
        return BasicDAO.instance
