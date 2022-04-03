import pytest
from src import app

app.config.update({
    "TESTING": True,
})

@pytest.fixture()
def client():
    return app.test_client()
