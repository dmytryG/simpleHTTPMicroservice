import asyncio

from DB.BasicDAO import BasicDAO
from DB.ListDB import ListDB
from DB.PGDB import PGDB

db: BasicDAO


async def init():
    global db
    db = ListDB.get_instance()


asyncio.run(init())
