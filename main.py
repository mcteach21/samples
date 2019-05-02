from termcolor import colored

from _vars import init as init1
from _tuples import init as init2
from _files import init as init3

nb = -1
menu_color = 'blue'
func_list = [init1, init2, init3]


def main():
    print("**************************************")
    print("Python : Samples & Tests")
    print("**************************************")


if __name__ == '__main__':  # si script courant
    main()


def menu():
    print(colored("************** Menu *******************", menu_color))
    print(colored("1- Variables & Declaration", menu_color))
    print(colored("2- Tuples & List", menu_color))
    print(colored("3- Dictionary..", menu_color))
    print(colored("4- All!", menu_color))
    print(colored("0- Quit!", menu_color))
    print(colored("***************************************", menu_color))

    global nb

    try:
        nb = int(input("choice (1-4, 0 to quit!) ==> "))
        exec_function(nb)

    except Exception as e:  # (RuntimeError, TypeError, NameError):
        print(colored("(x) Error : " + str(e) + "! try again.", 'red'))
        menu()


def all():
    print('all..')
    for f in func_list:
        f()


def get_func(num):
    return func_list[num - 1]


def exec_function(arg):
    # dictionary
    switcher = {
        0: lambda: print("Bye!!"),
        1: init1,
        2: init2,
        3: init3,
        4: all,
    }
    func = switcher.get(arg, lambda: print(colored("(x) unknown function! try again.", 'red')))
    print("(!) func (exec.) ==> " + func.__name__)
    return func()


while nb != 0:
    menu()
