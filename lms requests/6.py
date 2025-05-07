from requests import get

responce = get(f"http://{input()}").json()
names = [f"{user_data["last_name"]} {user_data["first_name"]}" for user_data in responce]
for i in sorted(names):
    print(i)

