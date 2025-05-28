# Client
# python client.py

import requests
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get server host from environment variable, default to 'server' for Docker
SERVER_HOST = os.getenv('SERVER_HOST', 'server')
SERVER_URL = f'http://{SERVER_HOST}:5000/hello'


if __name__ == '__main__':
    print("Client")
    while True:
        try:
            response = requests.get(SERVER_URL)
            print(f"Response from server: {response.json()['message']}", flush=True)
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to server: {e}", flush=True)
        time.sleep(5)
else:
    pass