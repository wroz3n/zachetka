import math as m 
choose = ""
result = float()
argument = float()

while True:
    choose = input("Выберете вариант : \n1. Логарифм \n2. Тригометрия \n3. Выход\nВаш выбор: ")
    
    if choose == "1":
        choose = input("Введите номер функций (1-4): ")
        argument = float(input("Введите x: "))
        try:
            if choose == "1":
                result = logarifm_f(argument)
            elif choose == "2":
                result = logarifm_two(argument)
            elif choose == "3":
                result = logarifm_three(argument)
            elif choose == "4":
                result = logarifm_four(argument)
            else:
                print("Неверный вариант!\n")
                continue
        except ValueError:
            print("Введено некорректное значение x. Введите корректное число.")
            continue
        print(f"f(x) = {format(result, '.6f')}\n")
    
    elif choose == "2":
        choose = input("Введите номер функций (1-4): ")
        argument = float(input("Введите x: "))
        try:
            if choose == "1":
                result = trigax_f(argument)
            elif choose == "2":
                result = trigax_two(argument)
            elif choose == "3":
                result = trigax_three(argument)
            elif choose == "4":
                result = trigax_four(argument)
            else:
                print("Неверный вариант!\n")
                continue
        except ValueError:
            print("Введено некорректное значение x. Введите корректное число.")
            continue
        print(f"f(x) = {format(result, '.6f')}\n")
    
    elif choose == "3":
        break
    else:
        print("Неверный вариант")
# Пример 1
# def logarifm_f(x: float ) -> float:
#     return m.log(x+3) + m.exp(x-2) - m.log10(m.exp(x-3)) / 2*x-1
# Пример 2
def logarifm_two(x: float ) -> float:
    return abs(m.log1p(m.factorial(x))) + m.pow(m.log(x+2, 2), 1/4)- 1/m.sqrt(m.log1p(x))
# Пример 3
def logarifm_three(x: float ) -> float:
    return m.log10(x**2 + 1) * 1/m.exp(x-1) - 1/m.pow(x, m.log1p(x+2))
# Пример 4
def logarifm_four(x: float) -> float:
    return m.log(x+1,5)/m.sqrt(m.exp(x-2)) - m.log10(3*x/2*x**3 - 1)



# Пример 5
def trigax_f(x: float) -> float:
    return (m.sin(x)**3 * m.cos(2*x)) / abs(m.tan(x/2))**2 + (1/m.tan(3*x))**2
# Пример 6
def triga_two(x:float ) -> float:
    return m.sqrt(abs( m.pow(m.sin(3*x),2) + m.pow(m.cos(x), 2) / m.cos(2*x) - 1))    * m.exp(m.sin(2*x + 1) * 1/m.tan(x-1))

# Пример 7
def triga_three(x:float) -> float:
    return (m.asin(x)**2) + m.exp(m.acos(x) - 1) / (m.sqrt(abs(m.atan(x/2))) * m.pi)   * (m.asin(abs(x))/x- m.pi)
# Пример 8
def triga_four(x:float) -> float:
    return (m.exp(m.fabs(m.pi/2 - m.atan(x))) - m.pi) / m.sqrt(m.acos(x)**2 + 1) - m.exp(x**2) / (m.pi + 3 * m.atan(x)**2)

