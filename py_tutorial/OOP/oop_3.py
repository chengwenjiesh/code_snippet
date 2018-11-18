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

    # -- class method should only be relevant with class, not instance
    @classmethod
    def set_raise_amount(cls, raise_amount):
        cls.raise_amount = raise_amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # -- static method should not be relevant to both class and instance
    @staticmethod
    def is_even(num):
        return num % 2 == 0

def main():
    emp_1 = Employee('John', 'Smith', 50000)
    emp_2 = Employee('Eric', 'Grant', 60000)
    Employee.set_raise_amount(1.06)
    print emp_1.raise_amount
    print emp_2.raise_amount
    emp_1.raise_pay()
    emp_2.raise_pay()
    print emp_1.pay
    print emp_2.pay

    emp_3 = Employee.from_string('Steve-Doe-70000')
    print emp_3.email
    print emp_3.fullname()

    print Employee.is_even(4)

if __name__ == '__main__':
    main()
