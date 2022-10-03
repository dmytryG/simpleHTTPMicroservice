from aiohttp import web
from aiohttp.web_routedef import Request

# Handler imports here
from Handlers.RegistrationHandler import register

# "Hello world" handler, it only reads name param from the get requests and answers with "Hello, {name}"
# It's not really interesting, right?


async def handle(request: Request):
    name = request.query['name']
    return web.Response(text="Hello, {name}!".format(name = name))

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/register', register)])

if __name__ == '__main__':
    web.run_app(app)
