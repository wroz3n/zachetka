from reg import registration
from auth import authorization
def start_menu():
    while True:
        start_input = input("Вы тут впервые или хотите войти в свой аккаунт (R/A) )")
        if start_input.upper() == "R":
            registration()
            break
        elif start_input.upper() == "A":
            authorization()
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 'R' для регистрации или 'A' для входа в свой аккаунт.")
start_menu()