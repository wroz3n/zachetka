from main_menu import data
import json
def admin_menu():
    while True:
        print('Admin menu is succefully started!')
        print ('For admin commands cheks pleas !help')
        admin_input = input('Choose what you wanna do: ')
        match admin_input:
            case '!delete':
                delete_user_input = input('Which you want to delete from users? (Enter name)')
                users = data.get('users', [])
                new_users = [user for user in users if user['username'] !=delete_user_input]

                data['users'] = new_users
                with open('user_data.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)

            case '!delete_all':
                delete_all_user_input = input('You wipe all users account, are you sure?')
                for data_user in data["users"]:
                    updated_data = {}
                    for key, value in data_user.items():
                        if key == delete_all_user_input:
                            updated_data.update({key : value})
                        else:
                            removed_value = value
                            print(f"User {removed_value} is succeully deleted.")
                    else:
                        print('Error')
                with open('user_data.json', 'w') as json_file:
                    json.dump (updated_data, json_file, indent=4)
            case "!add_user":
                    add_user_input = input('Add user: ')
                    add_password_input = input('Add password: ')
                    new_user = {"username": add_user_input, "password": add_password_input}
                    data["users"].append(new_user)
                    b = [i for i in data["users"]]
                    if new_user['username']not in b["username"]:
                        print(f"New user: '{new_user['username']}' created ")
                    else:
                        print(f"Username : {new_user['username']} already used")
                    with open('user_data.json', 'w') as json_file:
                        json.dump(data, json_file, indent=4)
            case "!all_users":
                print(f"All users:")
                for user in data["users"]:
                    print(user)
            case "!ban_user":
                ban_user_input = input('Which user you want to ban? (Enter name)')
                users = data.get('users', [])
                new_users = [user for user in users if user['username']!=ban_user_input]
                data['users'] = new_users
                with open('user_data.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                    print(f"User: '{ban_user_input}' is banned")
                gx = "banned_list.json"
                with open(gx, 'w') as json_file:
                    json.dump(ban_user_input, json_file, indent=4)
                    print('Ban list is updated')
                    
            case '!help':
                print('In these block you can watch your commands, now available: !help, !delete, !delete_all, !add_user for return to menu write "R"')
                print('for back to register choose command !unlogin')
            
            case '!exit':
                print('Close the program...')
                break

            case '!unlogin':
                pass