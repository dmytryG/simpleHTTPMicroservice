from aiohttp.web_routedef import Request
from aiohttp import web

from DB.BasicDAO import BasicDAO
from Models.Response import Response


async def all_users(request: Request):
    try:
        db = await BasicDAO.get_instance()

        users = await db.get_all_users()

        return web.Response(text=Response(False, users).to_JSON())

    except Exception as e:
        return web.Response(text=Response(True, str(e)).to_JSON())
