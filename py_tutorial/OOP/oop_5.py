class Employee(object):

    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_of_emp += 1

    def fullname(self):
        print '{} {}'.format(self.first, self.last)

    def raise_pay(self):
        self.pay = int(self.raise_amount * self.pay)

    def __repr__(self):
        print 'repr \n'
        return 'Employee({} {} {})'.format(self.first, self.last, self.pay)

    def __str__(self):
        print 'str \n'
        return 'Employee({} {} {})'.format(self.first, self.last, self.pay)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.first) + len(self.last)


def main():
    emp_1 = Employee('John', 'Smith', 50000)
    emp_2 = Employee('Eric', 'Grant', 60000)
    print emp_1
    print emp_2
    print emp_1 + emp_2
    print len(emp_1)


if __name__ == '__main__':
    main()
