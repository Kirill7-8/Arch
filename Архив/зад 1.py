import os
import shutil
import zipfile
def enter():
    input("\nНажмите Enter для продолжения...\n")

print('Добро пожаловать в программу! Для продолжения нажмите на "Enter"')

enter()

print(f"1. Текущая директория \n{os.getcwd()}")

enter()

print(f"2. Логин пользователя: \n{os.getlogin()}")

enter()

print("3. Тип операционной системы: \nWindows" if os.name == "nt" else "3. Тип операционной системы: Unix-подобная")

enter()

print('4. Проверка на наличие файла "test.txt"')
print('Файл "test.txt": существует' if os.path.isfile("test.txt") else 'Файл "test.txt": не существует')

enter()

print(f"5. Содеримое текущей папки: \n{os.listdir()}")

enter()

print("6. Файловая структура текущей директории с учётом вложенностей")

for roots, dirs, files in os.walk(os.getcwd()):
        print(f"Текущая директория: {roots}")
        print(f"Поддиректории: {dirs}" if len(dirs) > 0 else f"Поддиректории: Пусто")
        print(f"Файлы: {files}" if len(files) > 0 else f"Файлы: Пусто")
        print("-" * 150)

enter()

if os.path.isdir("test"):
    print('7. Папка "test" уже существует')
else:
    os.makedirs("test")
    print('7. Создана папка "test"')

enter()

os.chdir(f"{os.getcwd()}\\test")
print(f"8. Вы перешли в новую диреторию! Ваш новый путь:\n{os.getcwd()}")

enter()

name = input("9. Напишите название файла, который вы хотите создать: \n")
try:
    with open(name, "w+", encoding="utf-8") as file:
        file.write(os.getlogin())
except FileNotFoundError:
    name = "None"
    with open(name, "w+", encoding="utf-8") as file:
        file.write(os.getlogin())
print(f'В файл "{name}" записано и'
      f'мя пользовтеля')

enter()

print(f"10. Проверка файла {name}...")
if os.path.isfile(name) or os.path.isfile(name):
    if os.path.isdir(name) and os.path.isfile(name):
        print(f"В директории существует папка и файл с названием {name}")
    else:
        print(f'Файл с названием "{name}" успешно был создан' if os.path.isfile(name) else f'В директории находится только папка "{name}"')
else:
    print(f'Ошибка при создании файла "{name}"')

enter()

print(f'11. Абсолютный путь до файла "{name}": \n{(path_name := os.path.abspath(name))}')
print(f'Размер файла "{os.path.getsize(name)}" байт')

enter()

print(f"12. Директория на уровено выше: \n{(par_dic := os.path.dirname(os.getcwd()))}")
shutil.copy(path_name, par_dic)
print(f'Файл "{name}" был скопирован в родительскую директорию!')

enter()

os.chdir(par_dic)
print(f'13. Текущая дериктория: {os.getcwd()}')

for roots1, dirs1, files1 in os.walk(os.getcwd()):
        print(f"Текущая директория: {roots1}")
        print(f"Поддиректории: {dirs1}" if len(dirs1) > 0 else f"Поддиректории: Пусто")
        print(f"Файлы: {files1}" if len(files1) > 0 else f"Файлы: Пусто")
        print("-" * 150)

enter()

print(f'14. Содержимое файла "{name}":')
with open(name, "r", encoding="utf-8") as file1:
    print(file1.read())

enter()

print(f'15. Удаление папки "test"...')
shutil.rmtree("test")

enter()

print(f'16. Удаление файла "{name}" из текущей директории...')
os.remove(name)

enter()

print(f'17. Проверка на удаление папки "test" и файла "{name}"')
print('Удаление папки "test" прошло успешно!' if not os.path.isfile("test") else "Ошибка при удалении файла!")
print(f'Удаление файла "{name}" прошло успешно!' if not os.path.isdir("test") else "Ошибка при удалении папки!")

enter()

print("Архивирование")

enter()

shutil.make_archive("zipka","zip", os.getcwd())

print("Создан архив текущей папки")

zip_path = os.path.abspath("zipka.zip")
with zipfile.ZipFile("zipka.zip", "r") as zf:
    for roots1, dirs1, files1 in os.walk(zip_path):
        print(f"Текущая директория: {roots1}")
        print(f"Поддиректории: {dirs1}" if len(dirs1) > 0 else f"Поддиректории: Пусто")
        print(f"Файлы: {files1}" if len(files1) > 0 else f"Файлы: Пусто")
        print("-" * 150)





