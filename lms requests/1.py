from requests import get
response = get("http://127.0.0.1:5000")
print(response.content.decode("utf-8"))