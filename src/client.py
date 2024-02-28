import requests


class RequestClient:

    def _request(self, method, path, params=None, json=None, data=None):
        call = getattr(requests, method)
        response = call(url=path, params=params, json=json, data=data)
        response.raise_for_status()
        return response

    def get(self, path, params=None):
        return self._request(method='get', path=path).content
        return response.content
    
    def chuck(self, path='https://api.chucknorris.io/jokes/random'):
        return self._request(method='get', path=path)