import os

def Interface():
    nameP = input('Как вас зовут? ')
    print('Рады вас видеть', nameP)
    print('Что хотите сделать\n1)Создать файл\n2)Прочитать файл\n3)Дописать файл\n4)Редактировать файл\n5)Удалить файл')
    dei = int(input())
    if dei == 1:
        creat_file()
    
    elif dei == 2:
        read_file()
    
    elif dei == 3:
        change_file()
        
    elif dei == 4:
        change_silno_file()
        
    elif dei == 5:
        delete_file()
        
    else:
        print('У меня только три деиствия, напиши цифру от 1 до 5')
    return Interface
    

def creat_file():
    naz_file = input('Название файла и расширение json/csv: ')
    new_file = open(naz_file, "w")
    text = input()
    new_file.write(text)
    new_file.close()
    
    return Interface


def read_file():
    print("Чтение файла")
    print("Все папки и файлы:", os.listdir())
    naz_file = input('Напишите имя файла: ')
    new_file = open(naz_file, "r")
    new_file.close()
    
    
    return Interface


def change_file():
    print('Изменение файла')
    print("Все папки и файлы:", os.listdir())
    redak = input('Напишите имя файла: ')
    new_file = open(redak, "a")
    text = input()
    new_file.write(text)
    new_file.close()
    
    return Interface


def change_silno_file():
    print('Редактирование файла')
    print("Все папки и файлы:", os.listdir())
    redak = input('Напишите имя файла: ')
    new_file = open(redak, "r+")
    text = input()
    new_file.write(text)
    new_file.close()
    
    return Interface

def delete_file():
    print('Удаление файла')
    print("Все папки и файлы:", os.listdir())
    udol = input('Напишите имя файла: ')
    os.remove(udol)
    
    return Interface

Interface()