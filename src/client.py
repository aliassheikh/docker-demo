import requests


class RequestClient:

    def _request(self, method, path, params=None, data=None, json=None):
        call = getattr(requests, method)
        response = call(url=path, params=params, data=data, json=json)
        response.raise_for_status()
        return response

    def get(self, path, params=None):
        return self._request(method='get', path=path, params=params)
    
    def chuck(self, path='https://api.chucknorris.io/jokes/random', params=None):
        return self._request(method='get', path=path, params=params)