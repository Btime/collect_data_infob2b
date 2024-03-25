from src.controller.infob2b_controller import GetData
from src.controller.get_auth_controller import GetAuthorizationInfoB2B
from time import sleep
import json

def json_read():
    with open('authorization.json') as file:
        data = json.load(file)
        auth = data['token']
        return auth

def start():
    start_get_auth = GetAuthorizationInfoB2B()
    start_requests = GetData()

    try:
        auth = json_read()
    except:
        start_get_auth.run()
        auth = json_read()

    request_orders = start_requests.handle_process(token_authorization=auth)

    if request_orders == False:
        start_get_auth.run()
        auth = json_read()

