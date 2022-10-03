from aiohttp.web_routedef import Request
from aiohttp import web

from Models.Response import Response
from Models.User import User
from installer import db


async def retrieve(request: Request):
    try:
        user_name = request.query['user_name']

        user = await db.retrieve_user(user_name)

        return web.Response(text=Response(False, user).toJSON())

    except Exception as e:
        return web.Response(text=Response(True, str(e)).toJSON())
