import requests

# headers = {
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
#     'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryVXf5vAThRTthDKIf',
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
#     'CodeIdm': (None, '{"code":"eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsIng1dCI6IlMxRFJFM0lFZEhReWcwSlhhWWVMZEZrVHE4ZyIsImtpZCI6Im9yYWtleSJ9.eyJvcmFjbGUub2F1dGgucmVkaXJlY3QtdXJpIjoiaHR0cHM6Ly93d3cucG9ydGFsaW5mb2IyYi5jb20uYnIvbG9naW4iLCJzdWIiOm51bGwsIm9yYWNsZS5vYXV0aC51c2VyX29yaWdpbl9pZF90eXBlIjoiTERBUF9VSUQiLCJvcmFjbGUub2F1dGgudXNlcl9vcmlnaW5faWQiOiI4MDkzOTEwMiIsImlzcyI6Ind3dy5vcmFjbGUuZXhhbXBsZS5jb20iLCJvcmFjbGUub2F1dGguc3ZjX3BfbiI6IlZpdm9TZXJ2aWNlUHJvZmlsZSIsImlhdCI6MTcxMTM2OTMxMCwib3JhY2xlLm9hdXRoLnRrX2NvbnRleHQiOiJhemMiLCJleHAiOjE3MTEzNjk2MTAsInBybiI6bnVsbCwianRpIjoiNTVjYzdlYTktYjdhYy00ZDEzLTkyYjgtNTg1M2EwMjQ4ZTcwIiwib3JhY2xlLm9hdXRoLnNjb3BlIjoiQVBJTWFuYWdlci5EZWZhdWx0IFBvcnRhbEluZm9CMkIuRGVmYXVsdCIsIm9yYWNsZS5vYXV0aC5jbGllbnRfb3JpZ2luX2lkIjoiNzYzMWIyNmIxM2YyNDhlYzkzMmJhYjBiN2FjNjUzZjMiLCJ1c2VyLnRlbmFudC5uYW1lIjoiVml2byIsIm9yYWNsZS5vYXV0aC5pZF9kX2lkIjoiNGZlMTM5ZjctNWZjOS00NzE0LWE0ZjItZDAxNTM5YjFhZjg2In0.TeN_2QZzo8-4K4Omhk2K-NSXWymN1sIkdXOQ7pP9tWKKon1EUxS-4nx6kZU4_2EoPG9MHNdpoVt9uTF30xGarzAeIk0CfOa28mM6ve2nyG1wtAyOM6BDyxeW7i-YEcpFWjWQiXTlry0fBLwSx9pNQ-1VxTsdWVDWVZnyFiXQU0s"}'),
# }

# response = requests.post('https://apisegmentacao.portalinfob2b.com.br/API/Seguranca/CodeIdm', headers=headers, files=files)