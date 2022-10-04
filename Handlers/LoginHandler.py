from aiohttp.web_routedef import Request
from aiohttp import web

from DB.BasicDAO import BasicDAO
from Models.Response import Response
from Models.User import User


async def login(request: Request):
    try:
        db = await BasicDAO.get_instance()

        user_name = request.query['user_name']
        user_password = request.query['password']

        user = User(user_name, user_password)

        is_logged_in = await db.login(user)

        return web.Response(text=Response(False, is_logged_in).to_JSON())

    except Exception as e:
        return web.Response(text=Response(True, str(e)).to_JSON())
