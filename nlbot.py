import random
import telebot

# наш токен
token = ""

# переменная, в которой будут содержаться всем функции, которые нам нужны для обработки и ответа на сообщения
bot = telebot.TeleBot(token)

RANDOM_TASKS = ["Сходить в магазин", "Посмотреть фильм", "Покормить кошку", "Помыть машину", "Пропылесосить"]

HELP = """
# /help - вывести список доступных команд
# /start - приветствие
# /add or /todo - добавить задачу в список (название задачи запрашиваем у пользователя)
# /show - напечатать все добавленные задачи
# /random - добавить случайную задачу на дату Сегодня
# /exit - выход
"""

tasks = {}

# функция для проверки и добавления даты(ключ) в словарь и задачи в список задач(значение) 
def add_todo(date, task):
  date = date.lower()
  if date in tasks:
        # Дата есть в словаре
        # Добавляем в список задачу
        tasks[date].append(task)
  else:
      tasks[date] = [task]

# регистрация функции и сама функция команды "help"
@bot.message_handler(commands=["help"])
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
    date = command[1]
    task = command[2].lower()
    if len(task) < 3:
        bot.send_message(message.chat.id, "Задачи должны быть больше 3-х символов")
    else:
        add_todo(date, task)
        bot.send_message(message.chat.id, f"Задача {task} добавлена на дату {date}")

# регистрация функции и сама функция команды "random"
@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo("сегодня", task)
    bot.send_message(message.chat.id, f"Задача {task} добавлена на сегодня")

# регистрация функции и сама функция команды "show"
@bot.message_handler(commands=["show"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1]
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

# регистрация функции и сама функция команды "exit"
@bot.message_handler(commands=["exit"])
def exit(message):
    command = message.text
    bot.send_message(message.chat.id, "До новых встреч!")


# постоянно обращается к серверам телеграм, long_polling
bot.polling(none_stop=True)




