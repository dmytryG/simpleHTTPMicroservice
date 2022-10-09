# Simple HTTP microservice
## Simple educational project

---
## Datasource
There are two kinds of databases used in this project
1. ListDB - debug/educational-only database based on python list collection
2. PostgreSQL - more "real" case of databse using

To select, what DB will be used and configure it's parameters, use .env file

- Databases should implement DAO base class, which is presented in DB/BasicDAO.py.
DAO defines interface for all the used method and gives a way to standardize calls,
so, when you add another way to store your data (for e.g. you can migrate to SQLLight),
you whole program will not be shocked, because the new added datasource will be
wrapped.
- In order to use DAO, you have to have standardized models of your data. It can be hashmap,
list and even tuple, but the better way is to have custom class, that represents your
data, the model class. It can encapsulate all your data and give a clear representation
of it.
- Since working with database is I/O operations, it's a good approach to make all the
DB operations on async manner in order to reduce downtime and increase responsiveness.
- Since, you only have to have a small amount of connections to DB (because creating 
a new connection for each request will be time, memory, net and CPU-consuming operation)
we should use singleton pattern. So, when we're making a request to DB, we're making
a call to the same connection or a connection from pool.
- In order to make our code reusable and clear, we can use factory to create an instance
of DAO class.
---
## Handlers
There are several handlers in this project
- AllUsersHandler - get the list of all users
- LoginHandler - verify if user exists and it's password correct
- RegistrationHandler - create a new record of user
- RetrieveUserHandler - get a specified user
### All handlers in this project have similar architecture
```python
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

```
- In processing function we get an instance of DB
- Get all the necessary data from request
- Perform all the necessary manipulations on DB
- Complete the response

As a result we always return JSON of object response, again, in order to standardize
all the data.

Response class:
```python
class Response(Serializable):
    def __init__(self, is_err: bool, data):
        self.is_err = is_err
        self.data = data
```

Response example:
```json
{
    "data": [
        {
            "name": "User112",
            "password": "123"
        },
        {
            "name": "User3",
            "password": "123"
        }
    ],
    "is_err": false
}
```
In this project we're not using any MVC/MVP pattern, but it's better to be used. All 
business logic should be placed in controller and handler (view) only calls that logic and
sends representation of call results to end user.

Handlers also should be asynchronous due to system can be working with many users at
the same time, so, if we use synchronous approach, each user will have to wait till
previous requests will be processed. 

---
## Entry point
In python usually we have an entry point in main.py file. This file should not have 
any business logic. It should collect and setup all the necessary modules

---
## Config
In this project we get environment variables from .env file in config.py file,
using environs library. So, to configure the program, you only should make changes to
your .env file. It can make easier your interaction with software and especially
when deploying on server. Maybe, in python it's not really hard to change a
hardcoded string, but in compiling languages, it make a huge difference.

---
## Requirements.txt
```
aiohttp~=3.8.3
asyncpg~=0.26.0
environs~=9.5.0
```
This file collects all your project requirements, it's really useful to end user
and in process of deploying your project. You can call
```shell
pip install -r requirements.txt
```
in order to set up all the declared project requirements

---
# More specific to this project

---
## DB configuration
File .env contains DB connection properties

- DAO_CLASS - Class that will be set as a DB, there are two options (ListDB and PGDB) 

### if you're using PGDB class
- DB_USER - There you can specify your PG username
- DB_PASSWORD - There you can specify your PG password
- DB_NAME  - There you can specify your PG DB name
- DB_HOST - There you can specify the address of your database server 
(127.0.0.1 is localhost, default, if your DB is running on the same computer as app)

If you're interested in running example DB, you should deploy Examples/ExampleDB.sql on
your PostgreSQL server.

---
## Add your handler
If you want to add a custom handler, you just should define method, which accepts Request type
object as parameter and returns web.Response.

```python
async def custom_handler(request: Request):
    await do_things()
    return web.Response(text="some response")
```
In order to map this handler, you should modify the main file
```python
app.add_routes([web.get('/', handle),
                web.get('/custom', custom_handler)])
```
You can use decorators and classes to define handlers, more you can [find here](https://docs.aiohttp.org/en/stable/web_quickstart.html)

---
## Add your datasource
In order to add datasource, you can inherit BasicDAO class and implement all
the required methods specifically for your database. You'll also have to add
import to FactoryDAO class, in order to use .env to setup your project
```python
from DB.BasicDAO import BasicDAO
from DB.PGDB import PGDB
from DB.ListDB import ListDB
from DB.CustomDB import CustomDB
```
As DAO_CLASS in .env set the ___name___ of your class
```
DAO_CLASS=CustomDB
```

---
## How to run?
1. You have to configure DB
   1. Select your DB (ListDB or PGDB) in .env
   2. If you've selected ListDB, it's all that you need
   3. If you selected PGDB, you should deploy example DB from Examples/ExampleDB.sql to your
   PostgreSQL server. [How to do it](https://www.virtuozzo.com/application-platform-docs/dump-postgres/)
   4. Then, you have to configure DB_PASSWORD, DB_USER and DB_NAME. As DB_NAME select tha
   name of DB you've deployed, DB_PASSWORD and DB_USER if you're running default is same as
   in this project.
2. If you're using Windows, you just can run runner.bat script
3. Otherwise 
   1. you'll have to run `python -m venv venv` to create venv
   2. run `venv/Scripts/activate` to run your venv
   3. run `pip install -r requirements.txt` to install project requirements
   4. run `python ./main.py` to run the project

---
## Requests
Examples below are displayed on default setting, of course, you can change the
host and the port the way you want
### `localhost:8080/all`
Get all the users in db, returns
```json
    "data": [
        {
            "name": "User112",
            "password": "123"
        },
        {
            "name": "User3",
            "password": "123"
        }
    ],
    "is_err": false
```
### `localhost:8080/register?user_name=User3&password=123`
Adds new user to db, user_name and password should be transmitted as the get request 
parameters. Returns in good case:
```json
{
    "data": "User already registered",
    "is_err": true
}
```
OR in case of error
```json
{
    "data": null,
    "is_err": false
}
```
### `localhost:8080/login?user_name=User3&password=123`
Checks whether user is registred and password is correct, 
user_name and password should be transmitted as the get request 
parameters. Returns in good case:
```json
{
    "data": true,
    "is_err": false
}
```
OR in case of error (incorrect login data)
```json
{
    "data": false,
    "is_err": false
}
```
OR in case of error
```json
{
    "data": "User not found",
    "is_err": true
}
```
### `localhost:8080/retrieve?user_name=User1`
Gets user form DB, user_name should be transmitted as the get request 
parameters. Returns in good case:
```json
{
    "data": {
        "name": "User1",
        "password": "123"
    },
    "is_err": false
}
```
OR in case of error
```json
{
    "data": "User not found",
    "is_err": true
}
```