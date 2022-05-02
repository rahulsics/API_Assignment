import pytest
from payloads import payload
@pytest.fixture(autouse=True)
def set_up(request):
    baseUri = "https://reqres.in/api/users"
    yield baseUri

@pytest.fixture(scope="session", params=payload().t1_payload)
def test_data(request):
        yield request.param

@pytest.fixture(scope="session")
def schema_validate():
    return {'name': str, 'job': str, 'id':str, 'createdAt': str}