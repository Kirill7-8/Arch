from requests import get
total = 0
response = get(f"http://{input()}").json()
for item in response:
    if isinstance(item, int):
        total += item
print(total)