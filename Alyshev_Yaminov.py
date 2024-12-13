# Задание 1.
name = input("Введите свое имя: ");age  = int(input("Введите свой возраст: "));print(f"Привет, {name}! Тебе {age} лет!")
# Задание 2.
citys = ["Тюмень", "Казань", "Москва", "Мухосранск", "Екатеринбург"];x = ", ".join(citys);print(x)
# Задание 3.
number = int(input("Введите число: "))
if number % 2 ==0:
    print(f"Число {number} четно")
else:
    print(f"Число {number} не четно")
# Задание 4.
def summa():
    a = int(input("Введите первое число: "));b = int(input("Введите второе число: "))
    return (a+b)
print(summa())

# Задание 5.
slovar = {"Яблоко"  : 50,   "Банан" : 121,"Авакадо" : 163}
for s in slovar:
    print(f"{s} его цена : {slovar[s]} рублей")




# Задание 6
for i in range(1,11):
    print(i**2)

# Задание 7

while True:
    checlo = int(input("Введите число:"))
    if checlo == 0:
        break
# Задание 8.
numbers = []
for _ in range(6):
    num = float(input("Введите число "))
    numbers.append(num)

average = sum(numbers) / len(numbers)
print(f"Среднее значение: {average}")

# Задание 9
slovar = {"Яблоко"  : 50,   "Банан" : 121,"Авакадо" : 163}
fruit = input("Введите название фрукта: ")
if fruit in slovar:
    print(f"{fruit} найден, его цена {slovar[fruit]}")
else:
    print(f"Фрукт {fruit} не найден")

# Задание 10.
import random
numbx = []
for _ in range(6):
    random_num = random.randint(1,10)
    numbx.append(random_num)
print(sorted(numbx))

# Задание 11.
