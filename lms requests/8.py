from requests import post
from json import dumps

url = f"http://{input()}/users"
data = dumps({
    "username": input(),
    "last_name": input(),
    "first_name": input(),
    "email": input(),
})
post(url, data)
