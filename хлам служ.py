import requests
params = {"ll": "32.810152,39.889847",
                    "spn": "0.016457,0.00619",
                    "l": "map",
                    "apikey": "bbdf4eec-f4be-430d-acae-9f32d5c81f95",
                    
                    }
map_response = requests.get(f"https://static-maps.yandex.ru/1.x/?", params=params)
print(map_response)
with open("map.png", "wb") as file:
    file.write(map_response.content)