import pytest
from aiohttp import web

from app.main import app


@pytest.fixture
def cli(event_loop, aiohttp_client):
    """Fixture to create the aiohttp test client"""
    return event_loop.run_until_complete(aiohttp_client(app))


async def test_index(cli):
    """Test the index route."""
    resp = await cli.get("/")
    assert resp.status == 200
    text = await resp.text()
    assert text == "Hello, world!"
