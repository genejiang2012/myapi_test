import pytest
import requests


@pytest.fixture
def init_session():
    return requests.sessions.Session()


if __name__ == '__main__':
    init_session()