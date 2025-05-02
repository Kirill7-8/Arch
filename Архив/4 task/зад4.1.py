import json
import csv


def recreate_JSON():
    new_dict = {}
    with open("stars.csv", "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter="|")
        for row in reader:
            if row["Созвездие"] not in new_dict:
                new_dict[row["Созвездие"]] = {
                    "Созвездие": row["Созвездие"],
                    "Аббревиатура": row["Аббревиатура"],
                    "Площадь Созвездия (св. лет)": float(row["Площадь Созвездия (св. лет)"]),
                    "Название звезд": [],
                    "Ближайшее созвездия": row["Ближайшие созвездия"].split(", ")
                }
            new_dict[row["Созвездие"]]["Название звезд"].append({
                "Название звезды": row["Название звезды"],
                "Яркость": float(row["Яркость"])
            })

        res = []
        for const in new_dict.values():
            const["Название звезд"] = sorted(const["Название звезд"], key=lambda x: x['Яркость'])
            res.append(const)
        res.sort(key=lambda x: x['Созвездие'])
        with open("Const_recreated.json", "w", encoding="utf-8") as const_upt:
            json.dump(res, const_upt, indent=4, ensure_ascii=False)

def create_CSV():
    with open("Constellations1.json", "r", encoding="utf-8") as file:
        constellations = json.load(file)

    fields = ['Название звезды', 'Яркость', 'Созвездие', "Аббревиатура", "Площадь Созвездия (св. лет)", "Ближайшие созвездия"]
    with open('stars.csv', 'w', newline='', encoding="utf-8") as out_file:
        writer = csv.DictWriter(out_file, fieldnames=fields, delimiter="|")
        writer.writeheader()
        for const in constellations:

            for star in sorted(const['Название звезд'], key=lambda x: x['Яркость']):
                writer.writerow({'Название звезды': star["Название звезды"],
                             'Яркость': float(star["Яркость"]),
                             'Созвездие': const["Созвездие"],
                             "Аббревиатура": const["Аббревиатура"],
                             "Площадь Созвездия (св. лет)": float(const["Площадь Созвездия (св. лет)"]),
                             "Ближайшие созвездия": ", ".join(const["Ближайшее созвездия"])
            })

create_CSV()

recreate_JSON()




