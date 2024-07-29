
#Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
#Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
#Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
#Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.

def total_salary(path):
    with open(path, "r") as file:
        lines = file.readlines()
        #використовуємо file.readlines(), щоб прочитати всі рядки з файлу.
    
    salaries = []
    for line in lines:
        name, salary = line.split(',')
        #Для кожного рядка використовуємо line.split(','), щоб розділити його на ім'я та зарплату.
        salaries.append(float(salary.strip()))
        #Додаємо зарплату до списку salaries, використовуючи float(salary.strip()) для перетворення рядка на число.
    
    total = sum(salaries)
    #Обчислюємо загальну суму заробітної плати за допомогою sum(salaries).
    average = total / len(salaries) if salaries else 0
    #Обчислюємо середню заробітну плату, розділивши загальну суму на кількість зарплат (якщо список не порожній).
    
    return total, average


total, average = total_salary("D:\Курси\goit-algo-hw-04\Task 1\salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")