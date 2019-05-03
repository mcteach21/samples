from termcolor import colored

color = 'yellow'


def header(title):
    print("**************************************")
    print(colored(title, color))
    print("**************************************")


def printc(txt, _color='yellow'):
    print(colored(txt, _color))
