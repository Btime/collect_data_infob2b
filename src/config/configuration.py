import os
from dotenv import load_dotenv

load_dotenv()

AUTHORIZATION = os.getenv('AUTHORIZATION')
LOGIN_B2B = os.getenv('LOGIN_B2B')
PASSWORD_B2B = os.getenv('PASSWORD')