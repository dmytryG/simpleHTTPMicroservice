from aiohttp.web_routedef import Request
from aiohttp import web

from DB.BasicDAO import BasicDAO
from Models.Response import Response
from Models.User import User


async def register(request: Request):
    try:
        db = await BasicDAO.get_instance()

        user_name = request.query['user_name']
        user_password = request.query['password']

        user = User(user_name, user_password)

        await db.add_user(user)

        return web.Response(text=Response(False, None).to_JSON())

    except Exception as e:
        return web.Response(text=Response(True, str(e)).to_JSON())
