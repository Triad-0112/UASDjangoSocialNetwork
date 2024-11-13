import requests # type: ignore

url = "http://127.0.0.1:8000/accounts/login"

response = requests.get(url)

print(response.status_code)

print(response.cookies.get_dict())
