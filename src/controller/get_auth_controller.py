import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

# from src.config.configuration import LOGIN_B2B, PASSWORD_B2B

class GetAuthorizationInfoB2B:
    def __init__(self, headless=False) -> None:
        self.headless = headless
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

        try:
            self.driver = webdriver.Chrome(options=options)
            self.wait = WebDriverWait(self.driver, 3)
            self.driver.get(self.infob2b_url)
        except Exception as e:
            print(e)

    def login(self):
        try:
            # login_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.xpath_login['login_input']))).send_keys(LOGIN_B2B)
            # password_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.xpath_login['password_input']))).send_keys(PASSWORD_B2B)
            login_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.xpath_login['login_input']))).send_keys('80939102')
            password_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.xpath_login['password_input']))).send_keys('Nova@@2024')
            input('ENTER APÓS RESOLVER CAPTCHA')
            button_login = self.wait.until(EC.presence_of_element_located((By.XPATH, self.xpath_login['button_login']))).click()
            self.get_auth_header()
        except NoSuchElementException:
            print('No element found')
        except TimeoutException:
            print('Timeout')

    def get_auth_header(self):
        url = self.driver.current_url
        input('')
        response = requests.get(url)
        print(response.headers)
        print(response.request.headers)
        authorization_header = response.request.headers.get('Authorization')
        print("Authorization Header:", authorization_header)

    def run(self):
        self.load_xpath()
        self.load_browser()
        self.login()
        input('ENTER')

# if __name__ == '__main__':
#     start_get_auth = GetAuthorizationInfoB2B()
#     start_get_auth.run()
        



