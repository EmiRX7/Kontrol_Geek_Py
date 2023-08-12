import os

def Interface():
    nameP = input('Как вас зовут? ')
    print('Рады вас видеть', nameP)
    print('Что хотите сделать\n1)Создать файл\n2)Изменить файл\n3)Удалить файл')
    dei = int(input())
    if dei == 1:
        creat_file()
    
    elif dei == 2:
        change_file()
    
    elif dei == 3:
        print('Удаление файла')
    
    else:
        print('У меня только три деиствия, напиши цифру от 1 до 3')
    return Interface
    

def creat_file():
    naz_file = input('Название файла и расширение json/csv: ')
    new_file = open(naz_file, "w")
    text = input()
    new_file.write(text)
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
    

def delete_file():
    print('Удаление файла')
    print("Все папки и файлы:", os.listdir())
    udol = input('Напишите имя файла: ')
    os.remove(udol)
    
    return Interface

Interface()