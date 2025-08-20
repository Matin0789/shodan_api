import shodan
import logging
from shodan_utils import search_shodan

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def main(query):
    try:
        results = search_shodan(query)
        logging.info(f"Number of results: {results['total']}")

        for result in results['matches'][:5]:
            logging.info(f"IP: {result['ip_str']} | Port: {result['port']} | organization: {result.get('org', 'N/A')}")

    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    query = input("Please enter query:")
    main(query)