import os
from dotenv import load_dotenv

load_dotenv()
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")