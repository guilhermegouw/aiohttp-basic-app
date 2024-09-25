from aiohttp import web

from .routes import routes


def setup_routes(app):
    app.add_routes(routes)


app = web.Application()
setup_routes(app)


if __name__ == "__main__":
    web.run_app(app, port=8080)
