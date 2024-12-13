# Задание 1
class NegativeNumberError(Exception):
    def __init__(self,message,line):
        self.line  = line
        self.message = message
    def __str__(self):
        return f"{self.message}, at line {self.line}"
class AtributeNumber():
    def __init__(self,message:str):
        self.message = message

    def message_func(self):
        return self.message
    def pos_number(self,value: int):
        try:
            if value < 0:
                    raise NegativeNumberError('Number cannot be negative', 78)
            return f'{self.message}{value}'
        except NegativeNumberError as e:
            print(f'Caught an error at: {e}')

atribute_number = AtributeNumber('\nYour number: ')
print(atribute_number.pos_number(-4))
# Задание 2
class DataBaseError(Exception):
    def __init__(self, message, line):
        self.line = line
        self.message = message

    def __str__(self):
        return f"{self.message}, at line {self.line}"

class DataBase:
    def __init__(self):
        self.data = {}
        self.errors = []

    def message(self):
        return 'This is a database.'

    def connect_to_database(self, key, line):
        try:
            if key in self.data:
                raise DataBaseError('Key already exists', line)
            self.data[key] = line
        except DataBaseError as e:
            self.errors.append(f'Caught an error at: {e}')
            print(f'Error: {e}')

db = DataBase()
db.connect_to_database(21, 83)


#Зад 3
class InvalidAgeError(Exception):
    def __init__(self, message, line):
        super().__init__(message)
        self.line = line 

    def __str__(self):
        return f'{self.args[0]} at line {self.line}'

class User:
    def __init__(self, message: str):
        self.message = message 
    
    def get_message(self):
        return self.message
    
    def set_years(self, value: int):
        try:
            if value < 0 or value > 150:
                raise InvalidAgeError('Invalid age provided', 24)  
            return f'{self.message} {value}'
        except InvalidAgeError as e:
            print(f'Error: {e}')

user = User("User age is:");kk = int(input())
print(user.set_years(kk)) 

# Зад 4
class TooManyAttemptsError(Exception):
    def __init__(self, message, line):
        self.message = message
        self.line = line
    def __str__(self):
        return f'{self.message} at line {self.line}'
class Login():
    def __init__(self, correct_password):
        self.correct_password = correct_password
        self.attempts = 0
    def attempt_login(self,password):
        self.attempts += 1
        if self.attempts > 3:
            raise TooManyAttemptsError('Too many login attempts', 134)
        if password != self.correct_password:
            print('Неверный вход')
        else:
            print('Успешный вход')
login = Login("secret123")
try:
    login.attempt_login("secret123")
    login.attempt_login("wrongpass")
    login.attempt_login("wrongpass")
except TooManyAttemptsError as e:
    print(e)


# Зад 5
class EmptyStringError(Exception):
    def __init__(self, message, line):
        super().__init__(message)
        self.message = message
        self.line = line 

    def __str__(self):
        return f'{self.message} at line {self.line}'
    
class Logger():
    def __init__(self, filename: str):
        self.filename = filename
    
    def write_logs(self, error: EmptyStringError):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f'{error}\n')

def upper_funct(message: str):
    try:
        if len(message) == 0:
            raise EmptyStringError("Empty_String_Error", 17)
        return message.upper()
    except EmptyStringError as e:
        print(f'Caught an error: {e}')
        logger.write_logs(e)

logger = Logger('log.txt')
print(upper_funct(input()))