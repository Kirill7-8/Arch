from requests import get
import sys
adress = input()
i = input()
text = sys.stdin.readlines()
try:
    request = get(f"http://{adress}/users/{i}").json()
    for line in text:
        #**request возвращает значения вида "ключ"="значение"
        #format подставляет эти самые значения в строку 
        print(line.format(**request), end="") #end нужен, тк в конце каждой строки сохраняется \n
        
except ValueError:
    print("Пользователь не найден")
    

    