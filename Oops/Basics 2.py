class employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)    

emp_1 = employee('Rishika','Agarwal',50000)
emp_2 = employee('Test','User', 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(employee.fullname(emp_1))