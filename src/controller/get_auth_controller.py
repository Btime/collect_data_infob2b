import json
from src.utils.logs import Log
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.config.configuration import LOGIN_B2B, PASSWORD_B2B, TEMP_FOLDER, URL_INFO_B2B
import shutil
import os

class GetAuthorizationInfoB2B:
    def __init__(self, headless=False) -> None:
        self.headless = headless
        self.log = Log()
        self.token_authorization = None

    def load_xpath(self):
        self.xpath_login = {
            'login_input': '//*[@id="username"]',
            'password_input': '//*[@id="password"]',
            'button_login': '//*[@value="Entrar"]',
            'confirmation_login': '//*[@id="appheadercomponent"]'
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

        self.wait = WebDriverWait(self.driver, 30)
        self.driver.get(URL_INFO_B2B)

    def login(self, token_authorization=None):
        try:
            login_input = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, self.xpath_login['login_input'])
                )
            ).send_keys(LOGIN_B2B)

            password_input = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, self.xpath_login['password_input'])
                )
            ).send_keys(PASSWORD_B2B)

            input('ENTER APÓS RESOLVER CAPTCHA')

            button_login = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, self.xpath_login['button_login'])
                )
            ).click()

            confirmation_login = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, self.xpath_login['confirmation_login'])
                )
            )
            
            self.log.info(
                descricao=f"{self.login.__name__}. Login para coletar novo token de autorizacao realizado.",
            )

            authorization = self.collect_token_authorization(token_authorization)

            self.driver.close()

            self.remove_temp_folder(TEMP_FOLDER)

            return authorization

        except NoSuchElementException as e:
            print(e)
        except TimeoutException as e:
            print(e)

    def collect_token_authorization(self, token_authorization):
        find_request = self.driver.wait_for_request('/API/Usuario/GetCboUsuarioSubstituto')
        token_authorization = find_request.headers['Authorization']

        data = {
            'token': token_authorization,
        }

        with open('authorization.json', 'w') as file:
            json.dump(data, file)

        self.log.info(
            descricao=f"{self.collect_token_authorization.__name__}. Json com token de autorizacao criado.",
        )

        return data

    def remove_temp_folder(self, path_folder):
        try:
            if os.path.exists(path_folder):
                shutil.rmtree(path_folder)
                self.log.info(
                    descricao=f"{self.remove_temp_folder.__name__}. Pasta temporaria do seleniumwire removida com sucesso.",
                )
            else:
                self.log.info(
                    descricao=f"{self.remove_temp_folder.__name__}. Não existe pasta temporaria para remover.",
                )
        except Exception as e:
            self.log.info(
                descricao=f"{self.remove_temp_folder.__name__}. Erro ao remover pasta temporaria {e}",
            )

    def run(self):
        self.load_xpath()
        self.load_browser()
        token = self.login(token_authorization=None)

        return token