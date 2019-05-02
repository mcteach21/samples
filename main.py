from termcolor import colored

from _vars import init as init1
from _tuples import init as init2
from _dico import init as init3

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
    print(colored("3- Dictionary..", menu_color))
    print(colored("4- All!", menu_color))
    print(colored("0- Quit!", menu_color))
    print(colored("***************************************", menu_color))

    global nb

    try:
        nb = int(input("choice (1-4, 0 to quit!) ==> "))
        switch_number(nb)
    # except(RuntimeError, TypeError, NameError):
    #     # error("invalide number!")
    #     print(colored("(x) "+TypeError.__name__+"! try again.", 'red'))
    #     menu()
    except Exception as e:
        print(colored("(x) Error : " + str(e)+"! try again.", 'red'))
        menu()


# def error(mess):
#     print(colored("(x) "+mess+"! try again.", 'red'))


def all():
    init1()
    init2()
    init3()
    # menu()


def switch_number(arg):
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
