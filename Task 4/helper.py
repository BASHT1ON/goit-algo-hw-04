#Вимоги до завдання:

#Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
#Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду та її аргументи. Команди та аргументи мають бути розпізнані незалежно від регістру введення.
#Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій. В разі введення команди "exit" або "close", програма повинна завершувати виконання.
#Напишіть функції обробники для різних команд, такі як add_contact(), change_contact(), show_phone() тощо.
#Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
#Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.


#Ця функція розділяє введений користувачем рядок на команду та аргументи.
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

#Додає новий контакт до словника contacts.
def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: You must provide a username and a phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

#Змінює номер телефону для існуючого контакту.
def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: You must provide a username and a new phone number."
    name, phone = args
    if name not in contacts:
        return "Error: Contact not found."
    contacts[name] = phone
    return "Contact updated."

#Виводить номер телефону для заданого контакту.
def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: You must provide a username."
    name = args[0]
    if name not in contacts:
        return "Error: Contact not found."
    return f"The phone number for {name} is {contacts[name]}."

#Виводить всі збережені контакти.
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

#Головна функція, яка взаємодіє з користувачем і викликає відповідні функції для обробки команд.
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
