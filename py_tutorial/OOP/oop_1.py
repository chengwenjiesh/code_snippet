class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        print '{} {}'.format(self.first, self.last)


def main():
    emp_1 = Employee('John', 'Smith', 50000)
    emp_2 = Employee('Eric', 'Grant', 60000)
    print emp_1.email
    print emp_2.email
    print emp_1.fullname()
    print emp_2.fullname()
    print Employee.fullname(emp_1)
    print Employee.fullname(emp_2)


if __name__ == '__main__':
    main()
