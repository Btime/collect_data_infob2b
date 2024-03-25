import requests
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import json
import requests

# from src.config.configuration import LOGIN_B2B, PASSWORD_B2B

class GetAuthorizationInfoB2B:
    def __init__(self, headless=False) -> None:
        self.headless = headless
        self.token_authorization = None
        self.infob2b_url = 'https://www.portalinfob2b.com.br/login'

    def load_xpath(self):
        self.xpath_login = {
            'login_input': '//*[@id="username"]',
            'password_input': '//*[@id="password"]',
            'button_login': '//*[@value="Entrar"]',
        }

    def load_browser(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")

        if self.headless:
            options.add_argument("--headless")

        self.driver = webdriver.Chrome(
            options=options
            )
        
        self.wait = WebDriverWait(self.driver, 3)
        self.driver.get(self.infob2b_url)

    def login(self, token_authorization=None):
        try:
            login_input = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, self.xpath_login['login_input'])
                )
            ).send_keys('80939102')
            password_input = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, self.xpath_login['password_input'])
                )
            ).send_keys('Nova@@2024')
            input('ENTER APÓS RESOLVER CAPTCHA')
            button_login = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, self.xpath_login['button_login'])
                )
            ).click()
            find_request = self.driver.wait_for_request('/API/Usuario/GetCboUsuarioSubstituto')
            token_authorization = find_request.headers['Authorization']

            data = {
                'token': token_authorization,
            }

            sleep(1)

            with open('authorization.json', 'w') as file:
                json.dump(data, file)

            sleep(1)

            self.driver.close()

            return data

        except NoSuchElementException:
            print('No element found')
        except TimeoutException:
            print('Timeout')

    def run(self):
        self.load_xpath()
        self.load_browser()
        token = self.login(token_authorization=None)
        return token

# if __name__ == '__main__':
#     start_get_auth = GetAuthorizationInfoB2B()
#     start_get_auth.run()



