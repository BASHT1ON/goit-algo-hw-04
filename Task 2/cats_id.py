#Вимоги до завдання:

#Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
#Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
#Функція має повертати список словників, де кожен словник містить інформацію про одного кота.


def get_cats_info(path):
    cats = []
    # Створимо пустий список 
    with open(path, "r") as file:
        lines = file.readlines()
        #Прочитаємо файл.
    for line in lines:
        id, name, age = line.strip().split(',')
        #Розділимо кожен рядок на три частини:
        # унікальний ідентифікатор, ім'я кота та його вік.
        cat_info = {
            "id": id,
            "name": name,
            "age": age
        }
        #Створимо словник для кожного кота.
        cats.append(cat_info)
        #Додамо ці словники до списку.

    
    return cats


cats_info = get_cats_info("D:\Курси\goit-algo-hw-04\Task 2\Cats.txt")
print(cats_info)