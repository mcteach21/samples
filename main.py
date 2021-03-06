import datetime

from termcolor import colored

from _header import header
from _vars import init as init1
from _tuples import init as init2
from _files import init as init3
from classes.user import Student

nb = -1
menu_color = 'green'
func_list = [init1, init2, init3]


def main():
    header("Python : Samples & Tests")


if __name__ == '__main__':  # si script courant
    main()


def cls():
    import os
    import platform

    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


def all():
    print('all..')
    for f in func_list:
        f()


def get_func(num):
    return func_list[num - 1]


def class_test():
    header("Python : Class & Object")
    name = input('your name? : ')
    birthday = input('your birthday?(yyyy-mm-dd) : ')
    s = Student(**{'name': name, 'birthday': birthday})
    s.hello()

    # db = datetime.date(1901, 1, 31)
    # s2 = Student.fromJson('{"name": "' + name + '", "birthday": "' + str(db) + '"}')
    # s2.hello()
    print("**************************************")


def exec_function(arg):
    # dictionary
    switcher = {
        0: lambda: print("Bye!!"),
        1: init1,
        2: init2,
        3: init3,
        4: class_test,
        5: all,
        -1: cls,
    }
    func = switcher.get(arg, lambda: print(colored("(x) unknown function! try again.", 'red')))
    print("(!) func (exec.) ==> " + func.__name__)
    return func()


def menu():
    print(colored("************** Menu *******************", menu_color))
    print(colored("1- Variables & Declaration", menu_color))
    print(colored("2- Tuples, List, Dictionary", menu_color))
    print(colored("3- Files", menu_color))
    print(colored("4- POO", menu_color))
    print(colored("5- All!", menu_color))
    print(colored("0- Quit!", menu_color))
    print(colored("***************************************", menu_color))

    global nb

    try:
        nb = int(input("choice (1-4, 0 to quit!) ==> "))
        exec_function(nb)

    except Exception as e:  # (RuntimeError, TypeError, NameError):
        print(colored("(x) Error : " + str(e) + "! try again.", 'red'))
        menu()


while nb != 0:
    menu()
