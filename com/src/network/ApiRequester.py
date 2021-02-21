from com.src.passwords import COINMARKETCAP_API_KEY
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class ApiRequester:
    url = None
    parameters = None
    headers = None
    session = None

    def __init__(self, url: str, parameters: dict, headers: dict):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

        self.parameters = {
        
            'start':'1',
            'limit':'5000',
            'convert':'USD'
        }

        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
        }

        self.session = Session()
        self.session.headers.update(self.headers)

    def get(self):
        try:
            response = self.session.get(self.url, params=self.parameters)
            data = json.loads(response.text)
            print(data)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
