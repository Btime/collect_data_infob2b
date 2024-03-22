from seleniumwire import webdriver

driver = webdriver.Chrome()

driver.get('URL_DA_PAGINA')

driver.wait_for_request('URL_DA_REQUISICAO')

request = driver.requests[-1]  
headers = request.headers

print("Authorization Header:", headers.get('Authorization'))

driver.quit()
