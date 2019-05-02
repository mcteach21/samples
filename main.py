from termcolor import colored

from _vars import init as init1
from _tuples import init as init2


def main():
    print("**************************************")
    print("Python : Samples & Tests")
    print("**************************************")


def hello():
    print("hello from hello func.(main script)")


if __name__ == '__main__':  # si script courant
    main()

# hello()

nb = -1

menu_color = 'blue'


def menu():
    print(colored("************** Menu *******************", menu_color))
    print(colored("1- Variables & Declaration", menu_color))
    print(colored("2- Tuples & List", menu_color))
    print(colored("3- All!", menu_color))
    print(colored("0- Quit!", menu_color))
    print(colored("***************************************", menu_color))

    global nb

    try:
        nb = int(input("choice (1-3) ==> "))
        switch_number(nb)
    except:
        error("invalide number!")
        menu()


def error(mess):
    print(colored("(x) "+mess+"! try again.", 'red'))


def all():
    init1()
    init2()
    # menu()


def switch_number(arg):
    # dictionary
    switcher = {
        0: lambda: print("Bye!!"),
        1: init1,
        2: init2,
        3: all,
    }
    func = switcher.get(arg, error('unknown func!'))
    print("(!) func (exec0.) ==> " + func.__name__)
    return func()


while nb != 0:
    menu()
