import os
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.getenv('PASSW')
USER_NAME = os.getenv('USER')