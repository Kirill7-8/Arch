from requests import get
import sys
summa = 0
adress = input()
reqs = map(lambda x: x.strip(), sys.stdin.readlines())
for req in reqs:
    responce = get(f"http://{adress}{req}").json()
    summa += sum(responce)
print(summa)

