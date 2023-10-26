import random
import telebot

# наш токен
token = "6797118958:AAHZV9GwINMI8JXzHZyPtVOsb2FuTxP_bJ8"

# переменная, в которой будут содержаться всем функции, которые нам нужны для обработки и ответа на сообщения
bot = telebot.TeleBot(token)
# регистрация функции ниже в качестве обработчика сообщений типа text. Синтаксис декоратор.
@bot.message_handler(content_types=["text"])

# функция начинает отправку запросов к серверам telegram, используя token
def echo(message):
    bot.send_message(message.chat.id, message.text) # просто ответ на сообщение. Первый параметр - чат (уникальный идентификатор)

# постоянно обращается к серверам телеграм, long_polling
bot.polling(none_stop=True)

HELP = """
help - напечатать справку по программе.
add  - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи
exit - выход

* random - добавить случайную задачу на дату 'Сегодня'
"""

RANDOM_TASKS = ["Сходить в магазин", "Посмотреть фильм", "Покормить кошку", "Помыть машину"]

tasks = {

}

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
  print("Задача", task, "добавлена на дату", date)


while True:
    command = input("Введите команду:\n")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else: print("Такой даты нет")
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    elif command not in HELP:
        print("Неизвестная команда")
        break
