from requests import get
request = get(f"http://{input()}/users/{(i := input())}").json()
if int(i) < len(request):
    
else:
    print("Пользователь не найден")