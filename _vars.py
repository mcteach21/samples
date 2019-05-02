from termcolor import colored

txt = "global var text"


def header(title):
    print("**************************************")
    print(colored(title, 'yellow'))
    print("**************************************")


def init():
    header("Python : Variables & Declaration")

    a = 2608
    print("var a = " + str(a))

    name = "mc"
    print("var name = " + name)

    a = "coucou"
    print("var a (redeclare) = " + a)

    global txt  # global var
    print("var txt : " + txt)
    txt = "value changed!!"

    # del txt # delete var!
    print("**************************************")


if __name__ == '__main__':  # si script courant
    print("txt : " + txt)
    init()
    print("txt : " + txt)
