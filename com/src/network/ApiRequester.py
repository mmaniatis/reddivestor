from com.src.passwords import COINMARKETCAP_API_KEY
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class ApiRequester:
    headers = None
    session = None

    def __init__(self):
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
        }

        self.session = Session()
        self.session.headers.update(self.headers)

    def get(self, url: str, parameters: dict):
        try:
            response = self.session.get(url, params=parameters)
            data = json.loads(response.text)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            return None