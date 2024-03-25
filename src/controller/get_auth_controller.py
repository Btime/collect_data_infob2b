import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
import json
import requests

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
        options.set_capability(
                        "goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"}
                    )
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

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
            self.get_auth()
        except NoSuchElementException:
            print('No element found')
        except TimeoutException:
            print('Timeout')

    def get_auth_header(self):
        log_entries = self.driver.get_log("performance")

        for entry in log_entries:
            log_data = json.loads(entry["message"])["message"]
            
            if log_data["method"] == "Network.requestWillBeSent":
                request_url = log_data["params"]["request"]["url"]
                
                if 'CodeIdm' in request_url:
                    document_url = log_data["params"]["documentURL"]
                    self.code_for_request = document_url.split("code=")[1]
                    self.headers = log_data["params"]["request"]["headers"]
                    return self.code_for_request


    def get_auth(self):   
        code_json = json.dumps({"code":self.code_for_request})

        try:
            headers = self.headers

            headers.update({
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'),
            })

            files = {
                'CodeIdm': (None, f'{code_json}'),
            }

        except Exception as e:
            print(e)

        response = requests.post('https://apisegmentacao.portalinfob2b.com.br/API/Seguranca/CodeIdm', headers=headers, files=files)
        print(response.status_code)
        print(response.text)

        if response.ok:
            print(response.json())

    # import requests

    # headers = {
    #     'accept': 'application/json, text/plain, */*',
    #     'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    #     'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryZWn6AwpB7c8YOR6a',
    #     'origin': 'https://www.portalinfob2b.com.br',
    #     'referer': 'https://www.portalinfob2b.com.br/',
    #     'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"Windows"',
    #     'sec-fetch-dest': 'empty',
    #     'sec-fetch-mode': 'cors',
    #     'sec-fetch-site': 'same-site',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    # }

    # files = {
        # 'CodeIdm': (None, '{"code":"eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsIng1dCI6IlMxRFJFM0lFZEhReWcwSlhhWWVMZEZrVHE4ZyIsImtpZCI6Im9yYWtleSJ9.eyJvcmFjbGUub2F1dGgucmVkaXJlY3QtdXJpIjoiaHR0cHM6Ly93d3cucG9ydGFsaW5mb2IyYi5jb20uYnIvbG9naW4iLCJzdWIiOm51bGwsIm9yYWNsZS5vYXV0aC51c2VyX29yaWdpbl9pZF90eXBlIjoiTERBUF9VSUQiLCJvcmFjbGUub2F1dGgudXNlcl9vcmlnaW5faWQiOiI4MDkzOTEwMiIsImlzcyI6Ind3dy5vcmFjbGUuZXhhbXBsZS5jb20iLCJvcmFjbGUub2F1dGguc3ZjX3BfbiI6IlZpdm9TZXJ2aWNlUHJvZmlsZSIsImlhdCI6MTcxMTMzNTU5Miwib3JhY2xlLm9hdXRoLnRrX2NvbnRleHQiOiJhemMiLCJleHAiOjE3MTEzMzU4OTIsInBybiI6bnVsbCwianRpIjoiMjM2MzA4YzMtMjJiNy00M2FlLTljMWEtYTY3YWM4NTM1OWQzIiwib3JhY2xlLm9hdXRoLnNjb3BlIjoiQVBJTWFuYWdlci5EZWZhdWx0IFBvcnRhbEluZm9CMkIuRGVmYXVsdCIsIm9yYWNsZS5vYXV0aC5jbGllbnRfb3JpZ2luX2lkIjoiNzYzMWIyNmIxM2YyNDhlYzkzMmJhYjBiN2FjNjUzZjMiLCJ1c2VyLnRlbmFudC5uYW1lIjoiVml2byIsIm9yYWNsZS5vYXV0aC5pZF9kX2lkIjoiNGZlMTM5ZjctNWZjOS00NzE0LWE0ZjItZDAxNTM5YjFhZjg2In0.jb408nHJxsb6MHID-9pU_WbardDonLqlbb1zPlOAboaYM-ruv4h0JnTcCedCwlgYDv7narfHRV22zDaRjVtxCfWFhcHDly-UOO1tFL1sUDWTnbda4Q4vLcJJHXE7kyfi7tRdoitIvijDfMh8M_KvZ3-ZtVrJzlB9sm2Eht758bY"}'),
    

    # response = requests.post('https://apisegmentacao.portalinfob2b.com.br/API/Seguranca/CodeIdm', headers=headers, files=files)

    def run(self):
        self.load_xpath()
        self.load_browser()
        self.login()
        input('ENTER')

if __name__ == '__main__':
    start_get_auth = GetAuthorizationInfoB2B()
    start_get_auth.run()
        
