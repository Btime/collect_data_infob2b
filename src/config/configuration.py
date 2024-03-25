import os
from dotenv import load_dotenv

load_dotenv()

LOGIN_B2B = os.getenv('LOGIN_B2B')
PASSWORD_B2B = os.getenv('PASSWORD_B2B')
TEMP_FOLDER = r"C:\Users\teamb\AppData\Local\Temp\.seleniumwire"
URL_INFO_B2B = 'https://www.portalinfob2b.com.br/login'