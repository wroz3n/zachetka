import json
from keybebra import keyboard
from main_menu import main_menu
from main_menu import data
from main_menu import user
def registration():
    print("Registration!")
    reg_name_input = input("Введите новый логин: ")
    reg_pass_input = input("Введите новый пароль: ")
    user["username"] = reg_name_input
    user["password"] = reg_pass_input
    data["users"].append(user)
    with open ('user_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Вы успешно зарегистрировались, добро пожаловать {reg_name_input} Для продолжения нажмите Enter")
    if keyboard.wait('Enter'):
        print('Enter is pressed!')
        main_menu()
        