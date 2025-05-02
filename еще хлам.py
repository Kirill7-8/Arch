import json
with open("numbers.txt", "r") as file:
    s = [int(x.strip()) for x in file.read().split()]

    new_dict = {
        "count": len(s),
        "positive_count": len([x for x in s if int(x) >= 0]),
        "min": min(s),
        "max": max(s),
        "sum": sum(s),
        "average": float(f"{sum(s) / len(s):.2f}")
        }

    with open("statistics.json", "w") as f:
        json.dump(new_dict, f)