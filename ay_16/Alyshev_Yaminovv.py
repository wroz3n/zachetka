import math as m
# Арифмет. сумма - 1
def addition_first(e=0.000001) -> float:
    n = 1
    addit = 0
    while True:
        increment = 1/n
        addit += increment
        n += 1
        if m.fabs(increment) < e:
            break
    print(f"n = {n}")
    return addit
# Арифмет. сумма - 2
def adddition_two(e=0.000001) -> float:
    n = 1
    addit = 0
    while True:
        increment = n/m.pow(n,2)
        addit += increment
        n += 1
        if m.fabs(increment) < e:
            break
    print(f"n = {n}")
    return addit


# Арифмет сумма - 3
def adddition_three(e=0.000001) -> float:
    n = 2
    addit = 0
    while True:
        increment = m.log1p(n)/n
        addit += increment
        n += 1
        if m.fabs(increment) < e:
            break
    print(f"n = {n}")
    return addit


# Арифмет сумма - 4
def adddition_four(e=0.000001) -> float:
    n = 2
    addit = 0
    while True:
        increment = m.sin(n)/m.log10(n)
        addit += increment
        n += 1
        if m.fabs(increment) < e:
            break
    print(f"n = {n}")
    return addit


# Арифмет.произведение - 1
def multiplication_f(e=0.000001) -> float:
    n = 2
    multiplication = 1
    while True:
        increment = 1/ n * m.log(n)
        multiplication *= (1+increment)
        n += 1
        if m.fabs(increment) < e:
            break
        print(f"n = {n}")
        return multiplication
#Арифмет.произведение - 2
def multiplication_two(e=0.000001) -> float:
    n = 2
    multiplication = 1
    while True:
        increment = n/(n-1) * (n+2)
        multiplication *= (1+increment)
        n += 1
        if m.fabs(increment) < e:
            break
        print(f"n = {n}")
        return multiplication
# Арифмет.произведение - 3
def multiplication_three(e=0.000001) -> float:
    n = 1
    multiplication = 1
    while True:
        increment = m.cos(n)/m.sin(n**2)
        multiplication *= (1+increment)
        n += 1
        if m.fabs(increment) < e:
            break
        print(f"n = {n}")
        return multiplication
# Арифмет.произведение - 4
def multiplication_four(e=0.000001) -> float:
    n = 1
    multiplication = 1
    while True:
        increment =  m.pi/2  - m.atan(n)  / (m.e * n  - m.pi)
        multiplication *= (1+increment)
        n += 1
        if m.fabs(increment) < e:
            break
        print(f"n = {n}")
        return multiplication

choose = ""
result = float()
argument = float()

while True:
    choose = input("Выберете вариант : \n1. Арифметическая сумма. \n2. Арифметические произведения. \n3. Ваш выбор: ")
    
    if choose == "1":
        choose = input("Введите номер функций (1-4): ")
        argument = float(input("Введите x: "))
        try:
            if choose == "1":
                result = addition_first(int(argument))
            elif choose == "2":
                result = adddition_two(int(argument))
            elif choose == "3":
                result = adddition_three(int(argument))
            elif choose == "4":
                result = adddition_four(int(argument))
            else:
                print("Неверный вариант!\n")
                continue
        except ValueError:
            print("Введено некорректное значение x. Введите корректное число.")
            continue
        print(f"f(x) = {format(result, '.9f')}\n")
    
    elif choose == "2":
        choose = input("Введите номер функций (1-4): ")
        argument = float(input("Введите x: "))
        try:
            if choose == "1":
                result = multiplication_f(int(argument))
            elif choose == "2":
                result = multiplication_two(int(argument))
            elif choose == "3":
                result = multiplication_three(int(argument))
            elif choose == "4":
                result = multiplication_four(int(argument))
            else:
                print("Неверный вариант!\n")
                continue
        except ValueError:
            print("Введено некорректное значение x. Введите корректное число.")
            continue
        print(f"f(x) = {format(result, '.9f')}\n")
    
    elif choose == "3":
        break
    else:
        print("Неверный вариант")

