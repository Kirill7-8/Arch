import struct
import array

print("Выберите действие")
print("1. Изучить возможности библиотеки struct.")
print("2. Выгрузите в бинарный файл целое двухбайтное знаковое число")
print("3. Считайте из созданного бинарного файла беззнаковое двухбайтное число.")
print("4. Объясните полученный результат")
print("5. Повторите эти действия для других целых чисел, в том числе для граничных и выходящих за границы формата")
print("6. Повторите предыдущие действия для вещественных чисел.")
print("7. Было задумано вещественное число. Его записали в формате float с порядком байт big-endian.\n Затем из полученного файла прочитали два целых знаковых двухбайтных числа и получили ответ: -32641, 0. Какое число было задумано?")
print("8. Создайте скрипт, принимающий квадратный 24-разрядный рисунок в формате BMP")
choice = int(input())


def six(a=3.14, b=1e39, c=-1e39, d=1.7976931348623157e+308, e=-1.7976931348623157e+308, f=1.8e+308):
    print("float Хранит число в виде: 1 бит знака, 8 бит экспоненты, 23 бита мантиссы.")
    print(f"Для числа {a}")
    second(a, str(a), format="f")
    third(a, format="f")
    print("-" * 150)

    print(f"Для числа {b}")
    second(b, str(b), format="f")
    third(b, format="f")
    print("-" * 150)

    print(f"Для числа {c}")
    second(c, str(c), format="f")
    third(c, format="f")
    print("-" * 150)
    
    print(f"Для числа {d}")
    second(d, str(d), format="f")
    third(d, format="f")
    print("-" * 150)

    print(f"Для числа {e}")
    second(e, str(e), format="f")
    third(e, format="f")
    print("-" * 150)

    print("double Хранит число в виде: 1 бит знака, 11 бит экспоненты, 52 бита мантиссы.")
    print(f"Для числа {a}")
    second(a, str(a), format="d")
    third(a, format="d")
    print("-" * 150)

    print(f"Для числа {b}")
    second(b, str(b), format="d")
    third(b,format="d")
    print("-" * 150)

    print(f"Для числа {c}")
    second(c, str(c), format="d")
    third(c, format="d")
    print("-" * 150)
    
    print(f"Для числа {d}")
    second(d, str(d), format="d")
    third(d, format="d")
    print("-" * 150)

    print(f"Для числа {e}")
    second(e, str(e), format="d")
    third(e, format="d")
    print("-" * 150)

    print(f"Для числа {f}")
    second(f, str(f), format="d")
    third(f, format="d")
    print("-" * 150)

    print(f"Для числа {-f}")
    second(-f, str(-f), format="d")
    third(-f, format="d")
    print("-" * 150)

def five(a=32767, b=-32767, c=-32768, d=32768, e=-32769):
    print(f"Для числа {a}")
    second(a, str(a))
    third(a)
    print("-" * 150)

    print(f"Для числа {b}")
    second(b, str(b))
    third("-32767")
    print("-" * 150)

    print(f"Для числа {c}")
    second(c, str(c))
    print("-" * 150)
    
    print(f"Для числа {d}")
    second(d, str(d))
    print("-" * 150)

    print(f"Для числа {e}")
    second(e, str(e))
    print("-" * 150)

def third(file="-12345", format="H"):
    if file == "-12345":
        file = input("Введите название файла\n")

    with open(f"{file}.bin", "rb") as d:
        try:
            print(struct.unpack(format, d.readline())[0])
        except struct.error:
            print("struct.error: unpack requires a buffer of 4 bytes")

def second(num=-12345, file="-12345", format="h"):
    if num == -12345:
        num = int(input("Введите целое двубайтное число (от 32768 до -32768)\n"))
    elif file == "-12345":
        file = input("Введите название файла\n")
    try:
        num_packed = struct.pack(format, num)
    except struct.error:
        print("Превышен размер ячейки хранения памяти")

    with open(f"{file}.bin", "wb") as f:
        try:
            f.write(num_packed)
            print(f"Число: {num}\nЗапакованное: {num_packed}\nВ файле: {file}.bin")
        except UnboundLocalError:
            print("UnboundLocalError: cannot access local variable 'num_packed' where it is not associated with a value")

def seven():
    print("Пойдем от обратного")

    with open('file.bin', 'wb') as f:
        f.write(struct.pack('>hh', -32641, 0))

    with open('file.bin', 'rb') as f:
        print(f'Задуманное вещественное число: {struct.unpack('>f', f.read())[0]}')



def pic():
    with open('in.bmp', 'rb') as in_pic:
        head = in_pic.read(54)
        width = struct.unpack('<i', head[18:22])[0]
        height = struct.unpack('<i', head[22:26])[0]
        row_size = (width * 3 + 3) & ~3
        pixel_data = in_pic.read(row_size * height)
        main = array.array('B', pixel_data)

    with open('neg_pic.bmp', 'wb') as neg_pic:
        neg_pic.write(head)
        n = main[:]
        for i in range(len(n)):
            n[i] = 255 - n[i]
        neg_pic.write(n.tobytes())

    with open('light_pic.bmp', 'wb') as light_pic:
        light_pic.write(head)
        l = main[:]
        for i in range(len(l)):
            l[i] = min(255, l[i] + 100)
        light_pic.write(l.tobytes())

    with open('dark_pic.bmp', 'wb') as dark_pic:
        dark_pic.write(head)
        d = main[:]
        for i in range(len(d)):
            d[i] = max(0, d[i] - 100)
        dark_pic.write(d.tobytes())

    with open('gray_pic.bmp', 'wb') as gray_pic:
        gray_pic.write(head)
        g = main[:]
        for y in range(height):
            for x in range(width):
                index = y * row_size + x * 3
                b, g_val, r = g[index:index + 3]
                gray = int(0.3 * r + 0.59 * g_val + 0.11 * b)
                g[index] = g[index + 1] = g[index + 2] = gray
        gray_pic.write(g.tobytes())

    with open("inTest.bmp", "rb") as test, open('right_pic.bmp', 'wb') as right_pic:
        head = test.read(54)
        row_size = (width * 3 + 3) & ~3

        new_width = struct.unpack('<i', head[18:22])[0]
        new_height = struct.unpack('<i', head[22:26])[0]
        new_row_size = (width * 3 + 3) & ~3 & ~3
        new_image_size = new_row_size * new_height
        new_head = bytearray(head)
        new_head[18:22] = struct.pack('<i', new_width)
        new_head[22:26] = struct.pack('<i', new_height)
        new_head[34:38] = struct.pack('<i', new_image_size)

        rotated = array.array('B', [0] * new_image_size)

        for y in range(height):
            for x in range(width):
                src_index = y * row_size + x * 3
                new_x = height - y - 1
                new_y = x
                dest_index = new_y * new_row_size + new_x * 3
                rotated[dest_index:dest_index+3] = main[src_index:src_index+3]

        right_pic.write(new_head)
        right_pic.write(rotated.tobytes())

        
match choice:
    case 1:
        print("Библиотека struct изучена! (наверное)")
    case 2:
        num = int(input("Введите целое двубайтное число (от 32768 до -32768)\n"))
        second(num)
    case 3:
        third()
    case 4:
        print("Результат меняется не потому, что байты изменились, а потому что способ их интерпретации — другой.")
        print("При знаковой конвертации мы превращаем число через обратный код, то есть инвертируем биты, а потом добавляем 1")
        print("А при беззнаковой мы стандартно их превращаем")
    case 5:
        five()
    case 6:
        six()
    case 7:
        seven()
    case 8:
        pic()
        


