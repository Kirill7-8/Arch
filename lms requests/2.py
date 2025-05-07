from requests import get
adress = input()
total = 0
while True:
    response = int(get(f"http://{adress}").content.decode("utf-8"))
    if response != 0:
        total += response
    else:
        break
print(total)