import requests

session = requests.sessions.Session()

class BaseAPI:
    method = "GET"
    url = ""
    params = {}
    headers = {}
    data = {}
    json = {}
    cookies = {}

    def __init__(self):
        self.response = None

    def set_params(self, **params):
        self.params = params
        return self

    def set_data(self, data):
        self.data = data
        return self
    
    def set_json(self, json_data):
        self.json = json_data
        return self
    
    def set_cookies(self, key, value):
        self.cookies.update({key:value})
        return self
    
    def run(self, session=None):
        self.response = session.request(
            self.method,
            self.url, 
            cookies = self.cookies,
            params = self.params, 
            data = self.data, 
            json  = self.json,
            headers = self.headers    
        )
        return self
    
    def extract(self, field):
        value = self.response

        for _key in field.split("."):
            print("The key is {}, the value is {}, the type(value) is {}! \
                    ".format(_key, value, type(value)))
            if isinstance(value, requests.Response):
                if _key == "json()":
                    value = self.response.json()
                else:
                    value = getattr(value, _key)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict, dict)):
                value = value[_key]
        
        return value 
    
    def validate(self, key, expected_value):
        assert self.extract(key) == expected_value
        return self
    
    def get_response(self):
        return self.response