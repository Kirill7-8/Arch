import requests
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox, QVBoxLayout
from PyQt6.QtGui import QPixmap


class Map(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI task 1.1.ui', self)
        self.lineEdit.setPlaceholderText("Введите данные")
        self.Button.clicked.connect(self.geo)
        self.moreButton.clicked.connect(self.less)
        self.lessButton.clicked.connect(self.more)
        self.spn = [0.1, 0.1] 
        self.min_spn = 0.001   
        self.max_spn = 10.0     
        self.scale_factor = 1.5 
        self.flag = False

    def geo(self):
        if self.lineEdit.text():
            geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
            geocoder_params = {
                "apikey": "b38184af-37e2-490a-a06e-f28ce083824d",
                "geocode": self.lineEdit.text(),
                "format": "json"}
            response = requests.get(geocoder_api_server, params=geocoder_params)
            if response.status_code == 200:
                json_response = response.json()
                toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
                self.toponym_coordinates = toponym["Point"]["pos"]
                metadata = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]
                country = metadata["country_code"]
                postal_code = metadata.get("postal_code", "нет данных")
                components = metadata["Components"]
                city = next((comp["name"] for comp in components if comp["kind"] == "locality"), "нет данных")
                self.info_Label.setText(f'{toponym_address} "имеет координаты:" {self.toponym_coordinates}')
                full_info = f"Адрес: {toponym_address}\nКоординаты: {self.toponym_coordinates}\nСтрана: {country}\nГород: {city}\nПочт. индекс: {postal_code}"
                self.info_Label.setText(full_info)
                print(full_info)
                print(self.lineEdit.text())
                self.flag = True
                self.photo()
        else:
            QMessageBox(self, "Ошибка!", "Проверьте правильность введенных данных!")
            self.flag = False

    def photo(self):
        if self.flag == True:
            params = {
                "ll": ",".join(self.toponym_coordinates.split()),
                "spn": ",".join(map(str, [self.spn[0], self.spn[1]])),
                "l": "map",
                "apikey": "bbdf4eec-f4be-430d-acae-9f32d5c81f95",
            }
            map_response = requests.get(f"https://static-maps.yandex.ru/1.x/?", params=params)
            print(map_response)
            with open("map.png", "wb") as file:
                file.write(map_response.content)
            pixmap = QPixmap("map.png")
            self.photo_Label.setPixmap(pixmap)

    def less(self):
        new_spn = [self.spn[0] / self.scale_factor, self.spn[1] / self.scale_factor]
        if new_spn[0] >= self.min_spn and new_spn[1] >= self.min_spn:
            self.spn = new_spn
            self.photo()
            print(f"Увеличили масштаб: {self.spn}")

    def more(self):
        new_spn = [self.spn[0] * self.scale_factor, self.spn[1] * self.scale_factor]
        if new_spn[0] <= self.max_spn and new_spn[1] <= self.max_spn:
            self.spn = new_spn
            self.photo()
            print(f"Уменьшили масштаб: {self.spn}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Map()
    window.show()
    sys.exit(app.exec())