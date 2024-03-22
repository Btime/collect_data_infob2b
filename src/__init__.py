from src.controller.infob2b_controller import GetData
from src.controller.get_auth_controller import GetAuthorizationInfoB2B

def start():
    start_get_auth = GetAuthorizationInfoB2B()
    start_requests = GetData()

    start_get_auth.run()
    # start_requests.start_requests()