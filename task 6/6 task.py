from requests import get
response = [1, 2, "ошибка", 3]#get(f"http://{input()}").content.decode("utf-8")
total = sum(map(int, [x for x in response if isinstance(x, int)]))
print(total)