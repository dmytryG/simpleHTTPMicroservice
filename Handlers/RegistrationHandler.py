from aiohttp.web_routedef import Request
from aiohttp import web

from Models.User import User
from installer import db


async def register(request: Request):
    try:
        user_name = request.query['user_name']
        user_password = request.query['password']

        if user_name == "" or user_password == "":
            raise Exception("Missing fields")

        user = User(user_name, user_password)

        await db.add_user(user)

    except Exception as e:
        return web.Response(text="FAILED {e}".format(e=e))

    return web.Response(text="SUCCESS")