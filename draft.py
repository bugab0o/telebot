# LESSON 1

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

# LESSON 2

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

x = 1
while x <= 10:
    print(x)
    x += 1
print(x)