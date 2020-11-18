import os
from loguru import logger

from mytest_api.httpbin import *
from .conftest import *


logger.add('../log/log_{time}.log', rotation='500 MB')
logger.debug('this is the debug message')

def test_version():
    from mytest_api import __version__
    assert isinstance(__version__, str)


def test_httpbin_get(init_session):
    TestHttpbinGet().run(init_session) \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().headers.Host", "www.httpbin.org")


def test_httpbin_get_with_params(init_session):
    TestHttpbinGet() \
        .set_params(abc=123, xyz=456) \
        .run(init_session) \
        .validate("status_code", 200)


def test_httpbin_post(init_session):
    TestHttpbinPost() \
        .set_data({"abc": 123}) \
        .run(init_session) \
        .validate("status_code", 200)


def test_httpbin_with_params_share(init_session):
    user_id = "my123"
    TestHttpbinGet() \
        .set_params(user_id=user_id) \
        .run(init_session) \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().headers.Host", "www.httpbin.org") \
        .validate("json().url",
                  "http://www.httpbin.org/get?user_id={}".format(user_id))

    TestHttpbinPost() \
        .set_json({"user_id": user_id}) \
        .run(init_session) \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().url", "http://www.httpbin.org/post?abc=123") \
        .validate("json().headers.Accept", 'application/json') \
        .validate("json().json.user_id", "my123")


def test_httpbin_extract(init_session):
    api_run = TestHttpbinGet().run(init_session)
    status_code = api_run.extract("status_code")
    assert status_code == 200

    server = api_run.extract("headers.server")
    assert server == "gunicorn/19.9.0"

    accept_type = api_run.extract("json().headers.Accept")
    assert accept_type == "application/json"


def test_httpbin_setcookies(init_session):
    api_run = TestHttpBinGetCookies() \
        .set_cookies("freeform1", "123") \
        .set_cookies("freeform2", "456") \
        .run(init_session)

    freeform1 = api_run.extract("json().cookies.freeform1")
    freeform2 = api_run.extract("json().cookies.freeform2")

    assert freeform1 == "123"
    assert freeform2 == "456"


def test_httpbin_extract_cookies(init_session):
    freeform = TestHttpBinGetCookies() \
        .set_cookies("freeform", "123") \
        .run(init_session) \
        .extract("json().cookies.freeform")

    TestHttpbinPost() \
        .set_json({"freeform": freeform}) \
        .run(init_session) \
        .validate("status_code", 200) \
        .validate("json().json.freeform", freeform)


def test_httpbin_login_status(init_session):
    logger.debug(init_session)
  
    # step1: login and get the cookies
    TestHttpBinSetCookies().set_params(freeform='567').run(init_session)

    # step2:
    resp = TestHttpbinPost() \
        .set_json({"abc": 123}) \
        .run(init_session) \
        .get_response()

    request_headers = resp.request.headers

    assert "freeform=567" in request_headers['Cookie']
