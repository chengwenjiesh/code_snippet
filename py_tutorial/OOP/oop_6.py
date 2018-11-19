class Employee(object):
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print '{} {}'.format(self.first, self.last)

def main():
    emp_1 = Employee('John', 'Smith', 50000)
    print emp_1.fullname
    emp_1.fullname = 'new_John new_Smith'
    print emp_1.fullname
    del emp_1.fullname


if __name__ == '__main__':
    main()
