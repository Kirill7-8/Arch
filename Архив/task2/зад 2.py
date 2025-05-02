import os
import re

a = input("Введите букву с которой должно начаться имя файла\n")

for files in os.listdir(os.getcwd()):
    if re.match(rf"^{a}.{{5,}}\d.\.txt", files):
        with open(f"{files}", "r", encoding="utf-8") as z:
            file = z.read()

            times = re.findall(r"\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?\b", file)
            email = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z-]+\.[A-Za-z]{2,}\b", file)
            url = re.findall(r"\bhttps?://(?:www\.)?\S+\.[A-Za-z]{2,}(?:\s+)?\b", file)
            pip = re.findall(r"\b[a-zA-Z_]\w*\b", file)
            date = re.findall(r"\b(?:[0-2][0-9]|3[01])[./-](?:0[1-9]|1[0-2])[./-]\d{4}\b|\b\d{4}[./-](?:0[1-9]|1[0-2])[./-](?:[0-2][0-9]|3[01])\b", file)
            # ДД:ММ:ГГГГ ГГГГ:ММ:ДД
            dig = re.findall(r"\b\d+\.\d+\b", file)
            znak = re.findall(r"\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b", file)

            print(f"В файле {files}:")
            print(f"Времена: {times}" if len(times) != 0 else "Нет времен")
            print(f"email-адреса: {email}" if len(email) != 0 else "Нет email-адресов")
            print(f"url-адреса: {url}" if len(url) != 0 else "Нет url-адресов")
            print(f"Имена переменных Python: {pip}" if len(pip) != 0 else "Нет имён переменных Python")
            print(f"Даты: {date}" if len(date) != 0 else "Нет дат")
            print(f"Вещественные числа: {dig}" if len(dig) != 0 else "Нет вещественных чисел")
            print(f"Знаки: {znak}" if len(znak) != 0 else "Нет знак")
            print("-"*150)

