class Employee:

    def __init__(self, id, name, hours):
        self.id = id
        self.name = name
        self.hours = hours
        
    def count_payment(self):
        pass

class Fixed_salary(Employee):
    def __init__(self, id, name, hours, amount_of_salary):
        super().__init__(id, name, hours)
        self.amount_of_salary = amount_of_salary
    
    def count_payment(self):
        return self.amount_of_salary


class Comission(Employee):
    def __init__(self, id, name, hours, amount_of_salary, amount_of_sales):
        super().__init__(id, name, hours)
        self.amount_of_salary = amount_of_salary
        self.amount_of_sales = amount_of_sales

    def count_payment(self):
        return self.amount_of_salary + self.amount_of_sales * 50

    
class Hourly_Paid(Employee):

    def __init__(self, id, name, amount_of_salary, hours):
        super().__init__(id, name, hours)
        self.amount_of_salary = amount_of_salary
   
    def count_payment(self):
        return self.hours * 100


def calculate_all_salaries(employees):
    total_sum = 0
    for employee in employees:
        salary = employee.count_payment()
        print('ID-', employee.id, 'NAME:', employee.name, 'SALARY:',employee.amount_of_salary)
        total_sum += salary

    print('Sum that spent to workers', total_sum)

def productive_w(list_of_productivity, list_of_names):
    most_productivity, most_productive_person = 0, None
    least_productivity, least_productive_person = 100, None
    for i in range(len(list_of_productivity) - 1):
        if list_of_productivity[i] > most_productivity:
            most_productivity, most_productive_person = list_of_productivity[i], \
                list_of_names[i]
        if list_of_productivity[i] < least_productivity:
            least_productivity, least_productive_person = list_of_productivity[i], \
                list_of_names[i]

    print(f'Most productive {most_productive_person} his productivity {most_productivity}')
    print(f'Least productive {least_productive_person} his productivity {least_productivity}')


def calculate_productivity(employees):
    hours_in_week = 40
    list_of_productivity = []
    list_of_names = []
    for employee in employees:
        productivity = employee.hours / hours_in_week * 100
        print(employee.name, productivity)
        list_of_productivity.append(productivity)
        list_of_names.append(employee.name)
    productive_w(list_of_productivity, list_of_names)

manager = Fixed_salary(id=1, name='Jake', amount_of_salary=50000, hours=16)
secretary = Fixed_salary(id=2, name='Lili', amount_of_salary=60000, hours=20)
saler = Comission(id=3, name='Rose', amount_of_salary=40000, amount_of_sales=25, hours = 10)
worker = Hourly_Paid(id=4, name='Dora', amount_of_salary=45000, hours = 12)
secretary_for_change = Hourly_Paid(id=5, name='Dim', amount_of_salary=43000, hours = 10)

list_of_workers = [manager, secretary, saler, worker, secretary_for_change]
calculate_all_salaries(list_of_workers)
calculate_productivity(list_of_workers)
