# import main
#
# # hello()
# print("hello! i'm test module.")

# import sys
# from termcolor import colored, cprint
#
# # text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
# # print(text)
# # cprint('Hello, World!', 'green', 'on_red')
#
# text = colored('Hi folks!', 'red', 'on_yellow')
# print(text)

from _vars import init as init1
from _tuples import init as init2
from _files import init as init3

func_list = {init1, init2, init3}

for f in func_list:
    f()
    # print(f.__name__)
