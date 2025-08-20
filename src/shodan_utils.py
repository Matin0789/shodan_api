import shodan
from config import SHODAN_API_KEY

api = shodan.Shodan(SHODAN_API_KEY)

def search_shodan(query):
    return api.search(query)
