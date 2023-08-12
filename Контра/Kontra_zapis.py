def Interface():
    nameP = input('Как вас зовут? ')
    print('Рады вас видеть', nameP)
    print('Что хотите сделать\n1)Создать файл\n2)Изменить файл\n3)Удалить файл')
    dei = int(input())
    if dei == 1:
        creat_file()
    
    elif dei == 2:
        print('Изменение файла')
    
    elif dei == 3:
        print('Удаление файла')
    
    else:
        print('У меня только три деиствия, напиши цифру от 1 до 3')
    

def creat_file():
    print('Создание файла')
    new_file = open("New_file.txt", "w")
    text = input()
    new_file.write(text)
    new_file.close()
    
    return Interface


def change_file():
    print('Изменение файла')
    
    return Interface
    

def delete_file():
    print('Удаление файла')
    
    return Interface

Interface()