
import threading
def numbers():
    for i in range(1,11):
        print(i)
thread1 = threading.Thread(target=numbers)
thread2 = threading.Thread(target=numbers)
thread1.start()
thread2.start()

thread1.join()
thread2.join()


# Задание 2.
import threading
def numb():
     for i in range(1, 6):
         print(i)
def lett():
     for letter in ['a', 'b', 'c', 'd', 'e']:
          print (letter)
thread1 = threading.Thread(target=numb);thread2 = threading.Thread(target=lett);thread1.start();thread2.start();thread1.join();thread2.join()


# Задание 3
