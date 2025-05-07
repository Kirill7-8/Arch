from requests import get
request = get(f"http://{input()}/users/{(i := input())}").json()
if int(i) < len(request):
    i -= 1
    print(f'Письмо для: {request[i]["email"]}\
    Здравствуйте, {request[i]["last_name"]} {request[i]["first_name"]}\
    Мы рады сообщить вам о предстоящей акции! \
    Все подробности на нашем сайте \
    С уважением, команда тестового сервера!')
else:
    print("Пользователь не найден")