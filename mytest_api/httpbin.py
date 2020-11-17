from mytest_api.api import BaseAPI

class TestHttpbinGet(BaseAPI):
    url = "http://www.httpbin.org/get"
    headers = {"accept": "application/json"}
    method = "GET"
    params = None


class TestHttpbinPost(BaseAPI):
    url = "http://www.httpbin.org/post"
    headers = {"accept": "application/json"}
    method = "POST"
    params={"abc": 123}    

    def set_data(self, data):
        self.data = data
        return self

class TestHttpBinGetCookies(BaseAPI):
    url = "http://www.httpbin.org/cookies"
    headers = {"accept": "application/json"}
    method = "GET"
    params = {}

class TestHttpBinSetCookies(BaseAPI):
    url = "http://www.httpbin.org/cookies/set"
    headers = {"accept": "text/plain"}
    method = "GET"
    params = {}