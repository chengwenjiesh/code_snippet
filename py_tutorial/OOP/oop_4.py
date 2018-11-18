class Employee(object):
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        print '{} {}'.format(self.first, self.last)

    def raise_pay(self):
        self.pay = int(self.raise_amount * self.pay)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, lang):
         super(Developer, self).__init__(first, last, pay)
         self.lang = lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
         super(Manager, self).__init__(first, last, pay)
         if employees is None:
             self.employees = []
         else:
             self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print emp.fullname()

def main():
    dev_1 = Developer('John', 'Smith', 50000, 'Python')
    dev_2 = Developer('Eric', 'Grant', 60000, 'Java')
    mng_1 = Manager('David', 'Davenport', 80000, [dev_1])
    print mng_1.email
    print mng_1.print_emps()
    mng_1.add_emp(dev_2)
    print mng_1.print_emps()
    mng_1.remove_emp(dev_2)
    print mng_1.print_emps()

    print isinstance(dev_1, Employee)
    print isinstance(dev_1, Manager)

    print issubclass(Manager, Employee)
    print issubclass(Manager, Developer)

if __name__ == '__main__':
    main()
