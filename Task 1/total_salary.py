

def total_salary(path):
    with open(path, "r") as file:
        lines = file.readlines()
    
    salaries = []
    for line in lines:
        name, salary = line.split(',')
        salaries.append(float(salary.strip()))
    
    total = sum(salaries)
    average = total / len(salaries) if salaries else 0
    
    return total, average


total, average = total_salary("D:\Курси\goit-algo-hw-04\Task 1\salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")