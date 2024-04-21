import os

try:
    textcounter = 0
    graficcounter = 0
    tablecounter = 0
    print("Текущая директория:", os.getcwd())
    data = input('Введите путь к небходимой директории: ')
    os.chdir(data)
    for entry in os.scandir(data):
        if entry.is_file() and entry.name.endswith(".docx"):
            textcounter += 1
        if entry.is_file() and entry.name.endswith(".txt"):
            textcounter += 1
        if entry.is_file() and entry.name.endswith(".dat"):
            textcounter += 1
        if entry.is_file() and entry.name.endswith(".jpg"):
            graficcounter += 1
        if entry.is_file() and entry.name.endswith(".png"):
            graficcounter += 1
        if entry.is_file() and entry.name.endswith(".jpeg"):
            graficcounter += 1
        if entry.is_file() and entry.name.endswith(".xlsx"):
            tablecounter += 1
    print('количество текстовых файлов: ', textcounter)
    print('количество графических файлов: ', graficcounter)
    print('количество табличных файлов: ', tablecounter)
    if not os.path.isdir("Собранная статистика"):
         os.mkdir("Собранная статистика")
    os.chdir("Собранная статистика")
    with open("Статистика.txt", "w") as text_file:
        text_file.write('количество текстовых файлов: ')
        text_file.write(f"{textcounter}\n")
        text_file.write('количество графических файлов: ')
        text_file.write(f"{graficcounter}\n")
        text_file.write('количество табличных файлов: ')
        text_file.write(str(tablecounter))
    os.chdir(data)
    print("Статистика была записана в файл 'Статистика.txt' в папке 'Собранная статистика'")
    print("Текущая директория:", os.getcwd())

except NameError and FileNotFoundError:
    print('Введенно неверное имя директории')
