#put in fixtures so we can reuse the same app test clients

import pytest
from app import app 

@pytest.fixture(scope='module')
def test_app():
    with app.app_context():
        yield app.test_client()