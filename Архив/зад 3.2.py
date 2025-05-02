#Откройте файл CSV. На основании данных, содержащихся в этой таблице, выполните задания.
#Какое среднее количество осадков выпадало за сутки в осенние месяцы (сентябрь, октябрь, ноябрь)?
#Какая средняя температура была в те дни года, когда дул северный (С) ветер?
#Найдите процентное соотношение количества дней, когда дули ветры «В», «СВ» и «ЮВ».
#Создайте файл res.csv, в который вынесите информацию о днях с температурой  выше нуля градусов. Наименование столбцов должны быть как в исходной таблице.
import csv

osadki = []
Cveter = []
winds = {'В': 0, 'СВ': 0, 'ЮВ': 0}
with open("var2.csv", "r", encoding="utf-8") as csvfile:
    data = csv.DictReader(csvfile, delimiter=';')

for row in data:
    if row["Дата"].split()[1] in ["сентября", "октября", "ноября"]:
        osadki.append(float(row["Осадки"]))

for row in data:
    wind = row["Ветер"]
    if wind == "С":
        Cveter.append(float(row["Температура"]))
    if wind in winds:
        winds[row["Ветер"]] += 1

day = {"В": "Восточный", "СВ": "Северо-восточный", "ЮВ": "Юго-восточный"}
print(f"Cреднее количество осадков в осенние месяцы: {sum(osadki) / len(osadki):.2f}мм")
print("-" * 150)
print(f"Средняя температура при северном ветре: {sum(Cveter) / len(Cveter):.2f}°C")
print("-" * 150)
print("Процентное соотношение ветров:")
for win, k in winds.items():
    print(f"{day[win]}: {(k / len(data)) * 100:.2f}%")
with open("res.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, delimiter=";", fieldnames=data[0].keys())
    writer.writeheader()
    for row in data:
        if float(row["Температура"]) > 0:
            writer.writerow(row)
print("4. Файл res.csv с днями с температурой больше нуля создан")

