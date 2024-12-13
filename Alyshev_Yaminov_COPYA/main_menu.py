import json;from keybebra import keyboard;import random 

with open('User_data.json', 'r') as json_file:
    data = json.load(json_file)


user = data["users"][0]
username = user["username"]
user_password = user["password"]



def main_menu():
    print(f'//MAIN MENU')
    main = input("Включить игру(A)/ Выйти(R)")
    if main == "A":
        play_kubik1d6()
    else:
        exit()


if __name__ == "__main__":
    print('\n DEBUG: Script is run in this document')
else:
    print('Script is imported')

def play_kubik1d6():
    start_game = input("Хoтите сыграть? -- Да(R)/ Нет(A)")
    if start_game == "R":
        print('Кубик: ')
        keyboard.wait('Enter')
        print(f'Вы выбросили: {random.randint(1,6)}')
    elif start_game == "A":
        pass

def exit_kubik1d7():
    exitea = input("Вы уверены? Да(R)/ Нет(A)")
    if exitea  == "A":
        main_menu()
    elif exitea == "R":
        print("OK!")