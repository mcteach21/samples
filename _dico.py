from _header import header

users = {'homer': 40, 'marge': 28, 'bart': 25, 'lisa': 'unknown'}


def init():
    header("Python : Dictionary")

    print('homer => '+str(users['homer']))
    print("**************************************")