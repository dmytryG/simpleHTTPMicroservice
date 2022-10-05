from aiohttp import web
from aiohttp.web_routedef import Request

from DB.FactoryDAO import FactoryDAO

# Handler imports here
from Handlers.AllUsersHandler import all_users
from Handlers.LoginHandler import login
from Handlers.RegistrationHandler import register
from Handlers.RetrieveUserHandler import retrieve


# "Hello world" handler, it only reads name param from the get requests and answers with "Hello, {name}"
# It's not really interesting, right?


async def handle(request: Request):
    try:
        name = request.query['name']
        return web.Response(text="Hello, {name}!".format(name=name))

    except Exception as e:
        return web.Response(text="Hello, world!")


async def on_startup(app):
    print("HTTP server is running")
    await FactoryDAO.get_instance()


app = web.Application()
app.on_startup.append(on_startup)
app.add_routes([web.get('/', handle),
                web.get('/register', register),
                web.get('/retrieve', retrieve),
                web.get('/login', login),
                web.get('/all', all_users)])

if __name__ == '__main__':
    web.run_app(app)
