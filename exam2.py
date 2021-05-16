class Monitoring:
    def __init__(self, name, fixed_price, wage, surname, id, hour_worked, hourly_salary, quantity_of_sales, comissions):
        self.name = name
        self.fixed_price = fixed_price
        self.wage = wage + comissions
        self.comissions = 50*quantity_of_sales
        self.quantity_of_sales = quantity_of_sales
        self.surname = surname
        self.id = id
        self.hour_worked = hour_worked
        self.hourly_salary = hour_worked*100

    def total_sum(self):
        total = self.fixed_price + self.wage + self.hourly_salary
        print(f'{self.fixed_price}-{self.name}-{self.id}')
        print(f'{self.wage} - {self.name} - {self.id}')
        print(f'{self.hourly_salary} - {self.name} - {self.id}')
        return total
    def best_worker(self):
        if self.hour_worked > 37:
            print (f'{self.name} best workers')
        elif self.hour_worked < 20:
            print(f'{self.name} lazy worker')
        else:
            pass

class Menedjer(Monitoring):
    def __init__(self, name, fixed_price, surname, id, hour_worked):
        super().__init__(name, surname, id,  hour_worked, fixed_price)
    def oplata(self):
        a = self.hour_worked + self.fixed_price
        return a

class Secretary(Monitoring):
    def __init__(self, name, fixed_price,  surname, id, hour_worked):
        super().__init__(name, surname, id,  hour_worked, fixed_price)
    def oplata1(self):
        a1 = self.hour_worked + self.fixed_price
        return a1

class Secretary_To_Replace(Secretary):
    def __init__(self, name, hourly_salary, surname, id, hour_worked):
        super().__init__(name, surname, id,  hour_worked, hourly_salary)
    def oplata2(self):
        a_ = self.hour_worked + self.hourly_salary
        return a_


class Seller(Monitoring):
    def __init__(self, name, wage, comissions, surname, id, hour_worked, quantity_of_sales):
        super().__init__(name, surname, id,  hour_worked, wage, comissions, quantity_of_sales)
    def oplata3(self):
        a2 = self.hour_worked + self.wage
        return a2

class Department_worker(Monitoring):
    def __init__(self, name, hourly_salary, surname, id, hour_worked):
        super().__init__(name, surname, id, hour_worked, hourly_salary)
    def oplata4(self):
        a3 = self.hour_worked + self.hourly_salary
        return a3

m = Menedjer('Барсбек', 45000, 'Канаткулов', 1, 18)
m.oplata()
s = Secretary('Алымкул', 20000, 'Тилекбаев', 2, 38)
s.oplata1()
ss = Secretary_To_Replace('Жанар', 18000, 'Рыскулов', 6, 33)
ss.oplata2()
c = Seller('Айпери', 20000, 50, 'Шалымбекова', 3, 38, 20)
c.oplata3()
d = Department_worker('Бакыт', 20000, 'Рустамов', 4, 25)
d.oplata4()
d1 = Department_worker('Алтынай', 20000, 'Ширинбаева', 5, 40)
d1.oplata4()