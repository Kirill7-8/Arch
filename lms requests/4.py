from requests import get
responce = get(f"http://{input()}").json()
print(responce.get(input(), "No data"))
