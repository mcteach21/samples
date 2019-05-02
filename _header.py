from termcolor import colored

color = 'yellow'


def header(title):
    print("**************************************")
    print(colored(title, color))
    print("**************************************")


def printc(txt, color='yellow'):
    print(colored(txt, color))
