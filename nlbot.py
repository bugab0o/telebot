import random
import telebot

# наш токен
token = "6797118958:AAHZV9GwINMI8JXzHZyPtVOsb2FuTxP_bJ8"

# переменная, в которой будут содержаться всем функции, которые нам нужны для обработки и ответа на сообщения
bot = telebot.TeleBot(token)

RANDOM_TASKS = ["Сходить в магазин", "Посмотреть фильм", "Покормить кошку", "Помыть машину"]

HELP = """
# /help or /info - вывести список доступных команд
# /start - приветствие
# /add or /todo - добавить задачу в список (название задачи запрашиваем у пользователя)
# /show or /print - напечатать все добавленные задачи
# /random - добавить случайную задачу на дату Сегодня
# /exit or /stop or /end - выход
"""

tasks = {}

# функция для проверки и добавления даты(ключ) в словарь и задачи в список задач(значение) 
def add_todo(date, task):
  if date in tasks:
        # Дата есть в словаре
        # Добавляем в список задачу
        tasks[date].append(task)
  else: 
        # Даты в словаре нет
        # Создаем запись с ключом date
       tasks[date] = [] # tasks[date] = [task]
       tasks[date].append(task)

# регистрация функции и сама функция команды "help"
@bot.message_handler(commands=["help", "info"])
def help(message):
    bot.send_message(message.chat.id, HELP)

# регистрация функции и сама функция команды "start"
@bot.message_handler(commands=["start"])
def help(message):
    bot.send_message(message.chat.id,"Привет ✌️ ")
    bot.send_message(message.chat.id,"Планирование -наше всё, приступим? ✍🏻")

# регистрация функции и сама функция команды "add"
@bot.message_handler(commands=["add", "todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2].lower()
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

# регистрация функции и сама функция команды "random"
@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

# регистрация функции и сама функция команды "show"
@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

# регистрация функции и сама функция команды "exit"
@bot.message_handler(commands=["exit", "stop", "end"])
def exit(message):
    command = message.text
    bot.send_message(message.chat.id, "До новых встреч!")


# постоянно обращается к серверам телеграм, long_polling
bot.polling(none_stop=True)




