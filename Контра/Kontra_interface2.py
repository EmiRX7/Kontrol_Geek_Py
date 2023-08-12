def Interface():
    nameP = input('Как вас зовут?')
    print('Рады вас видеть', nameP)
    print('Что хотите сделать\n1)Создать файл\n2)Изменить файл\n3)Удалить файл')
    dei = int(input)
    if dei == 1:
        creat_file()
    if dei == 2:
        change_file()
    if dei == 3:
        delete_file()
    else:
        print('У меня только три деиствия, напиши цифру от 1 до 3')
    

def creat_file():
    print('Создание файла')



def change_file():
    print('Изменение файла')
    

def delete_file():
    print('Удаление файла')

Interface()