from aiohttp.web_routedef import Request
from aiohttp import web

from Models.Response import Response
from Models.User import User
from installer import db


async def login(request: Request):
    try:
        user_name = request.query['user_name']
        user_password = request.query['password']

        user = User(user_name, user_password)

        is_logged_in = await db.login(user)

        return web.Response(text=Response(False, is_logged_in).toJSON())

    except Exception as e:
        return web.Response(text=Response(True, str(e)).toJSON())
