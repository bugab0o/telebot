HELP = """
help - напечатать справку по программе.
add  - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи
exit - выход
"""

today = []
tommorow = [] 
other = []


while True:
    command = input("Введите команду:\n")
    if command == "help":
        print(HELP)
    elif command == "show":
        print("Какой день?")
        day = input()
        if day == "Сегодня":
            print(today)
        elif day == "Завтра":
            print(tommorow)
        elif day != "Сегодня" and "Завтра":
            print(other)
    elif command == "add":
        task = input("Введите название задачи:\n")
        date = input("Введите день (дату):\n")
        if date == "Сегодня": today.append(task)
        elif date == "Завтра": tommorow.append(task)
        else: other.append(task)
        print("Задача добавлена")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    elif command not in HELP:
        print("Неизвестная команда")
        break  # или run = False
    
