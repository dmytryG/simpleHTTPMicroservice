from aiohttp import web
from aiohttp.web_routedef import Request

# Handler imports here
from Handlers.LoginHandler import login
from Handlers.RegistrationHandler import register
from Handlers.RetrieveUserHandler import retrieve

# "Hello world" handler, it only reads name param from the get requests and answers with "Hello, {name}"
# It's not really interesting, right?

async def handle(request: Request):
    try:
        name = request.query['name']
        return web.Response(text="Hello, {name}!".format(name = name))

    except Exception as e:
        return web.Response(text="Hello, world!")

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/register', register),
                web.get('/retrieve', retrieve),
                web.get('/login', login)])

if __name__ == '__main__':
    web.run_app(app)
