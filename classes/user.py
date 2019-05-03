import datetime
import json

from _header import printc


class User(object):
    name = ''

    # constructor(s)
    # def __init__(self):
    #     self.name = 'Doe'

    def __init__(self, name=None):
        if not name:
            name = 'doe'
        self.name = name

    def hello(self):
        printc('hello, my name is ' + self.name.capitalize())


class Student(User):
    birthday = ''

    # No Overloading!!

    # def __init__(self):
    #     super().__init__()
    #     self.birthday = '?'

    # def __init__(self, name, birthday):
    #     # super(Student, self).__init__(name)
    #     super().__init__(name)
    #     self.birthday = birthday

    # args -- tuple of anonymous arguments
    # kwargs -- dictionary of named arguments
    def __init__(self, *args, **kwargs):
        # print(kwargs)
        super().__init__(kwargs.get('name'))
        self.birthday = kwargs.get('birthday')

    @classmethod
    def fromJson(cls, json_data):
        data = json.loads(json_data)
        # return Student(data['name'], data['birthday'])
        return Student(**{'name': data['name'], 'birthday': data['birthday']})

    def hello(self):
        # print('hello! I\'m a student. my name is ' + self.name)
        super().hello()
        printc('I was born on ' + self.birthday, 'blue')

    # def hello2(self, name):
    #     self.hello(name)
    #     print('..I\'m a student!')


# Test class
def main():
    # c = User()
    # c.hello("Homer")
    # s = Student()
    # s.hello2('Bart Simpson')

    # s = Student('liSA', '2000-08-26')

    s = Student(**{'name': 'liSA', 'birthday': '2000-08-26'})
    s.hello()

    db = datetime.date(1901, 1, 31)
    s2 = Student.fromJson('{"name": "MC", "birthday": "'+str(db)+'"}')
    s2.hello()


if __name__ == "__main__":
    main()
