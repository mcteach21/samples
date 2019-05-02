import re

from _header import header, printc

file_name = 'file.txt'


def set_utf8_console():
    import subprocess
    subprocess.call([r'switch_console_to_utf8.bat'])


def init():
    header("Python : Files")
    print('Open File (txt) : ' + file_name)

    with open(file_name, "rb") as f:
        contents = f.read().decode("UTF-8")

    set_utf8_console()
    print('switch console to utf8..')

    print('..Read File (txt) : \n')
    printc(contents)

    print()

    contents = re.sub('[’.,;!?»]', ' ', contents)
    # printc(contents, 'green')

    words_count = {}
    words = contents.split(' ')
    for w in words:
        if len(w.strip()) > 1:
            w = w.strip().lower()
            words_count[w] = 1 if not words_count.keys().__contains__(w) else words_count[w] + 1

    print('mot : occurences (nb.)')
    print('----------------------')
    for word, count in sorted(words_count.items(), key=lambda t: t[1], reverse=True):
        print(word + ' : ' + str(count))

    print("**************************************")
