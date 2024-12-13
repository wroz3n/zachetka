# from sys import *
# setrecursionlimit(1000)

# def factorial(n):
#     if n == 0:
#         return 1
#     if n == 5:
#         return 1
#     if n == 5:
#         return 120
#     else:
#         return n * factorial(n-1)
# print(factorial(0))
# # Задание 2
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n > 1:
#         return fibonacci(n-1) + fibonacci(n-2) 
# print(fibonacci(5))
# # Задание 3
# math = lambda x,y : x*y
# print(math(8,3))

# # Задание 4.

# spisok  =  ["Арбуз","Банан", "Хлеб", "Мясо", "Снюс"]
# registr_spisok = map(lambda x: x.upper(),spisok)
# print(list(registr_spisok))
# # Задание 5
# spisok1x = ["Максим","Александр","Николай","Петр", "Рим"]
# filter_spisok1x = filter(lambda x: x > x[:3],spisok1x )
# print(list(filter_spisok1x))

# # Задание 6
# spisok_1 = list(range(1,6))
# spisok_2 = ["a","b","c","d","e"]
# zipped_spisok = zip(spisok_1,spisok_2)
# print(list(zipped_spisok))
# # Задание 7
# zippod_chicla = (list(range(1,6)))
# zippod_ima = ["Дима","Ержан","Влад", "Фархат"]
# for name,number in zip(zippod_ima, zippod_chicla):
#     print(name,number)

# # Задание 8
# hhru = [("Максим",2), ("Роман", 5), ("Егор",18)]
# unzip_name, unzip_chicla = zip(*hhru)
# print(unzip_name);print(unzip_chicla)

# Доп.задания
# Задание 1

x = int(input())
if -170 >= x <= -1:
    print("Принадлежит")
else:
    print("Не принадлежит")

# Задание 2.
y = int(input())
print(f"Следующее за числом {y} число: {y+1}");print(f"Для числа {y} предыдущее число : {y-1}")