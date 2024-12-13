from main_menu import*
from admin_menu import admin_menu
def authorization():
        print('\n Welcome to authorization menu!')
        username_input = input("Enter your login:")
        password_input = input("Enter your password:")
        for data_user in data["users"]:
            if username_input.lower() == data_user["username"].lower() and password_input == data_user["password"].lower():
                print(f'\nWelcome back, {username_input}!')
                main_menu()
                break
            elif username_input.lower() == "admin" and password_input == "admin":
                print("Start admin panel...")
                admin_menu()
                break
            else:
                pass
        else:
            print("Incorrect data, please try agane.")


