### LESSON 1 ###

# print("Hello, world!")

# strings = ["Hello", "world"]
# numbers = [1, 2, 3, 4, 5]
# data = ["hello", 1]

# print(strings)
# print(numbers)
# print(data)

# summa = numbers + data
# print(summa)

# numbers.append(6)
# print(numbers)

# first = strings[0]
# second = strings[1]
# print(first)
# print(second)

# strings_length = len(strings)
# print(strings_length)

# s = sum(numbers)
# print(s)


# # cat: кошка
# # bat: летучая мышь

# # ключ : значение

# dictionary = {
#   "cat": "кошка",
#   "bat": "летучая мышь"
# }

# # print(dictionary)
# # cat = dictionary["cat"]
# # print(cat)

# countries = {
#   "Африка": ["Египет", "Конго", "ЮАР"],
#   "Азия": ["Китай", "Таиланд", "Индонезия"]
# }

# africa = countries["Африка"]
# print(africa)

# africa_key = "Африка"
# print(countries[africa_key])

# countries["Европа"] = ["Австрия", "Испания", "Италия"]
# print(countries)
# print(countries["Европа"])
# # countries[0] = "Hello"
# # print(countries)
# africa.append("Эфиопия")
# print(africa)
# print(countries)
# print(len(countries["Африка"]))


# name = input("Введите имя: ")
# print("Привет", name)

### LESSON 2 ###

# name = input("Введите имя: ")
# print(name)

# name1 = "Oleg"
# print(name == name1)

# name = input("Введите имя: ")
# login = "Oleg"

# if name == login:
#     # Выражение True
#     print("Hello", name)
# elif len(name) < 3:
#     print("Такое имя недопустимо")
# # elif name == "Yo":
# #     print("Yo, bro")
# else:
#     # Выражение False
#     print("Hello, user!")

# print("The end")

# 2.4 Циклы

# x = 1
# while x <= 10:
#     print(x)
#     x += 1
# print(x)

### LESSON 3 ###

# 3.1 Добработка программы

# HELP = """
# help - напечатать справку по программе.
# add - добавить задачу в список (название задачи запрашиваем у пользователя).
# show - напечатать все добавленные задачи."""

# tasks = {

# }

# run = True

# while run:
#   command = input("Введите команду: ")
#   if command == "help":
#     print(HELP)
#   elif command == "show":
#     print(tasks)
#   elif command == "add":
#     date = input("Введите дату для добавления задачи: ")
#     task = input("Введите название задачи: ")
#     if date in tasks:
#         # Дата есть в словаре
#         # Добавляем в список задачу
#         tasks[date].append(task)
#     else: 
#         # Даты в словаре нет
#         # Создаем запись с ключом date
#        tasks[date] = [] # tasks[date] = [task]
#        tasks[date].append(task)
#     print("Задача", task, "добавлена на дату", date)
#   else: 
#     print("Неизвестная команда")
#     break

# print("До свидания!")

# 3.2 Цикл for

# for i in [4, 5, 6]:
#     if i % 2 == 0:
#         print(i)

# HELP = """
# # help - напечатать справку по программе.
# # add - добавить задачу в список (название задачи запрашиваем у пользователя).
# # show - напечатать все добавленные задачи."""

# tasks = {

# }

# run = True

# while run:
#   command = input("Введите команду: ")
#   if command == "help":
#     print(HELP)
#   elif command == "show":
#     date = input("Введите дату для отображения списка задач: ")
#     if date in tasks:
#       for task in tasks[date]:
#         print('- ', task)
#     else:
#       print("Такой даты нет")
#   elif command == "add":
#     date = input("Введите дату для добавления задачи: ")
#     task = input("Введите название задачи: ")
#     if date in tasks:
#         # Дата есть в словаре
#         # Добавляем в список задачу
#         tasks[date].append(task)
#     else: 
#         # Даты в словаре нет
#         # Создаем запись с ключом date
#        tasks[date] = [] # tasks[date] = [task]
#        tasks[date].append(task)
#     print("Задача", task, "добавлена на дату", date)
#   else: 
#     print("Неизвестная команда")
#     break

# print("До свидания!")

# 3.3 Функции

# HELP = """
# # help - напечатать справку по программе.
# # add - добавить задачу в список (название задачи запрашиваем у пользователя).
# # show - напечатать все добавленные задачи.
# # random - добавлять случайную задачу на дату Сегодня"""

# RANDOM_TASK = "Записаться на курс по IT"
# tasks = {

# }

# run = True

# def add_todo(date, task):
#   if date in tasks:
#         # Дата есть в словаре
#         # Добавляем в список задачу
#         tasks[date].append(task)
#   else: 
#         # Даты в словаре нет
#         # Создаем запись с ключом date
#        tasks[date] = [] # tasks[date] = [task]
#        tasks[date].append(task)
#   print("Задача", task, "добавлена на дату", date)

  
# while run:
#   command = input("Введите команду: ")
#   if command == "help":
#     print(HELP)
#   elif command == "show":
#     date = input("Введите дату для отображения списка задач: ")
#     if date in tasks:
#       for task in tasks[date]:
#         print('- ', task)
#     else:
#       print("Такой даты нет")
#   elif command == "add":
#     date = input("Введите дату для добавления задачи: ")
#     task = input("Введите название задачи: ")
#     add_todo(date, task)
#   elif command == "random":
#     add_todo("Сегодня", RANDOM_TASK)
#     # if "Сегодня" in tasks:  
#     #   tasks["Сегодня"].append(RANDOM_TASK)
#     # else:
#     #   tasks["Сегодня"] = []
#     #   tasks["Сегодня"].append(RANDOM_TASK)
#   else: 
#     print("Неизвестная команда")
#     break

# print("До свидания!")

#def my_func(i): # название функции
#  if i > 2:     # тело функции
#    return i    # возвращаемое значение

#x = my_func(3)

#print(x)

# def multiply(a, b):
#   result = a * b 
#   return result

# c = multiply(3, 5)
# print(c)

# def multiply(a, b):
#   print("a = ", a)
#   print("b = ", b)
#   result = a * b 
#   return result

# c = multiply(3, 5)
# print(c)
# c = multiply(7, 5)
# print(c)
# c = multiply(3, 518)
# print(c)

# def print_hello():
#     print("Hello")
#     print("World")

# print_hello()
# print_hello()



# 3.4 Использование сторонних библиотек

# import random



# HELP = """
# # help - напечатать справку по программе.
# # add - добавить задачу в список (название задачи запрашиваем у пользователя).
# # show - напечатать все добавленные задачи.
# # random - добавлять случайную задачу на дату Сегодня"""

# RANDOM_TASKS = ["Сходить в магазин", "Посмотреть фильм", "Покормить кошку", "Помыть машину"]

# tasks = {

# }

# run = True

# def add_todo(date, task):
#   if date in tasks:
#         # Дата есть в словаре
#         # Добавляем в список задачу
#         tasks[date].append(task)
#   else: 
#         # Даты в словаре нет
#         # Создаем запись с ключом date
#        tasks[date] = [] # tasks[date] = [task]
#        tasks[date].append(task)
#   print("Задача", task, "добавлена на дату", date)

  
# while run:
#   command = input("Введите команду: ")
#   if command == "help":
#     print(HELP)
#   elif command == "show":
#     date = input("Введите дату для отображения списка задач: ")
#     if date in tasks:
#       for task in tasks[date]:
#         print('- ', task)
#     else:
#       print("Такой даты нет")
#   elif command == "add":
#     date = input("Введите дату для добавления задачи: ")
#     task = input("Введите название задачи: ")
#     add_todo(date, task)
#   elif command == "random":
#     task = random.choice(RANDOM_TASKS)
#     add_todo("Сегодня", task)
#   else: 
#     print("Неизвестная команда")
#     break

# print("До свидания!")


### LESSON 4 ###

# import telebot


# наш токен
# token = ""

# # переменная, в которой будут содержаться всем функции, которые нам нужны для обработки и ответа на сообщения
# bot = telebot.TeleBot(token)

# my_name = "Олег"
# # регистрация функции ниже в качестве обработчика сообщений типа text. Синтаксис декоратор.
# @bot.message_handler(content_types=["text"])

# # функция начинает отправку запросов к серверам telegram, используя token
# def echo(message):
#     if my_name in message.text:
#         text = "Ба! Знакомые все лица!"
#     else: 
#         text = message.text
#     bot.send_message(message.chat.id, message.text) # просто ответ на сообщение. Первый параметр - чат (уникальный идентификатор)


# bot.polling(none_stop=True) # постоянно обращается к серверам телеграм, long_polling.
# # ctrl + C - стоп для бота


### LESSON 5 ###

# import random


# HELP = """
# # help - напечатать справку по программе.
# # add - добавить задачу в список (название задачи запрашиваем у пользователя).
# # show - напечатать все добавленные задачи.
# # random - добавлять случайную задачу на дату Сегодня"""

# RANDOM_TASKS = ["Сходить в магазин", "Посмотреть фильм", "Покормить кошку", "Помыть машину"]

# tasks = {

# }

# run = True

# def add_todo(date, task):
#   if date in tasks:
#         # Дата есть в словаре
#         # Добавляем в список задачу
#         tasks[date].append(task)
#   else: 
#         # Даты в словаре нет
#         # Создаем запись с ключом date
#        tasks[date] = [] # tasks[date] = [task]
#        tasks[date].append(task)
#   print("Задача", task, "добавлена на дату", date)

  
# while run:
#   command = input("Введите команду: ")
#   if command == "help":
#     print(HELP)
#   elif command == "show":
#     date = input("Введите дату для отображения списка задач: ")
#     if date in tasks:
#       for task in tasks[date]:
#         print('- ', task)
#     else:
#       print("Такой даты нет")
#   elif command == "add":
#     date = input("Введите дату для добавления задачи: ")
#     task = input("Введите название задачи: ")
#     add_todo(date, task)
#   elif command == "random":
#     task = random.choice(RANDOM_TASKS)
#     add_todo("Сегодня", task)
#   else: 
#     print("Неизвестная команда")
#     break

# print("До свидания!")



# import telebot
# import random

# # наш токен
# token = ""

# bot = telebot.TeleBot(token)

# RANDOM_TASKS = ["Сходить в магазин", "Посмотреть фильм", "Покормить кошку", "Помыть машину"]

# HELP = """
# # /help or /info or /start or /menu - вывести список доступных команд
# # /add or /todo - добавить задачу в список (название задачи запрашиваем у пользователя).
# # /show or /print - напечатать все добавленные задачи.
# # /random - добавить случайную задачу на дату Сегодня
# """

# tasks = {}

# def add_todo(date, task):
#   if date in tasks:
#         # Дата есть в словаре
#         # Добавляем в список задачу
#         tasks[date].append(task)
#   else: 
#         # Даты в словаре нет
#         # Создаем запись с ключом date
#        tasks[date] = [] # tasks[date] = [task]
#        tasks[date].append(task)

# @bot.message_handler(commands=["help", "info", "start", "menu"])
# def help(message):
#     bot.send_message(message.chat.id, HELP)

# @bot.message_handler(commands=["add", "todo"])
# def add(message):
#     command = message.text.split(maxsplit=2)
#     date = command[1].lower()
#     task = command[2].lower()
#     add_todo(date, task)
#     text = "Задача " + task + " добавлена на дату " + date
#     bot.send_message(message.chat.id, text)

# @bot.message_handler(commands=["random"])
# def random_add(message):
#     date = "сегодня"
#     task = random.choice(RANDOM_TASKS)
#     add_todo(date, task)
#     text = "Задача " + task + " добавлена на дату " + date
#     bot.send_message(message.chat.id, text)

# @bot.message_handler(commands=["show", "print"])
# def show(message):
#     command = message.text.split(maxsplit=1)
#     date = command[1].lower()
#     text = ""
#     if date in tasks:
#         text = date.upper() + "\n"
#         for task in tasks[date]:
#             text = text + "[] " + task + "\n"
#     else:
#         text = "Задач на эту дату нет"
#     bot.send_message(message.chat.id, text)


# bot.polling(none_stop=True)


### пример из курса ###
# from random import choice

# import telebot

# token = ''

# bot = telebot.TeleBot(token)


# RANDOM_TASKS = ['Написать Гвидо письмо', 'Выучить Python', 'Записаться на курс в Нетологию', 'Посмотреть 4 сезон Рик и Морти']

# todos = dict()


# HELP = '''
# Список доступных команд:
# * print  - напечать все задачи на заданную дату
# * todo - добавить задачу
# * random - добавить на сегодня случайную задачу
# * help - Напечатать help
# '''


# def add_todo(date, task):
#     date = date.lower()
#     if todos.get(date) is not None:
#         todos[date].append(task)
#     else:
#         todos[date] = [task]


# @bot.message_handler(commands=['help'])
# def help(message):
#     bot.send_message(message.chat.id, HELP)


# @bot.message_handler(commands=['random'])
# def random(message):
#     task = choice(RANDOM_TASKS)
#     add_todo('сегодня', task)
#     bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня')


# @bot.message_handler(commands=['add'])
# def add(message):
#     _, date, tail = message.text.split(maxsplit=2)
#     task = ' '.join([tail])
#     add_todo(date, task)
#     bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')


# @bot.message_handler(commands=['show'])
# def print_(message):
#     date = message.text.split()[1].lower()
#     if date in todos:
#         tasks = ''
#         for task in todos[date]:
#             tasks += f'[ ] {task}\n'
#     else:
#         tasks = 'Такой даты нет'
#     bot.send_message(message.chat.id, tasks)


# bot.polling(none_stop=True)