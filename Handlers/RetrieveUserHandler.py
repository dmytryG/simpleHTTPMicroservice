from aiohttp.web_routedef import Request
from aiohttp import web

from DB.BasicDAO import BasicDAO
from Models.Response import Response


async def retrieve(request: Request):
    try:
        db = await BasicDAO.get_instance()

        user_name = request.query['user_name']

        user = await db.retrieve_user(user_name)

        return web.Response(text=Response(False, user).to_JSON())

    except Exception as e:
        return web.Response(text=Response(True, str(e)).to_JSON())
