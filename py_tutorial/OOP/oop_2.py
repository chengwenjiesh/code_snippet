class Employee:

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


def main():
    emp_1 = Employee('John', 'Smith', 50000)
    print Employee.num_of_emp
    emp_2 = Employee('Eric', 'Grant', 60000)
    print Employee.num_of_emp
    emp_1.raise_pay()
    emp_2.raise_pay()
    print emp_1.pay
    print emp_2.pay

    emp_1.raise_amount = 1.05
    print emp_1.raise_amount
    print emp_2.raise_amount
    print Employee.raise_amount

    Employee.raise_amount = 1.05
    print emp_1.raise_amount
    print emp_2.raise_amount
    print Employee.raise_amount


if __name__ == '__main__':
    main()
