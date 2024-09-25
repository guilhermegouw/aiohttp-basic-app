from aiohttp import web
from .views import index


routes = [
    web.get("/", index),
]
