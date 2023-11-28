"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, base_pay, hours_worked=0, commission_rate=0, bonus=0, contracts_landed=0):
        self.name = name
        self.contract_type = contract_type
        self.base_pay = base_pay
        self.hours_worked = hours_worked
        self.commission_rate = commission_rate
        self.bonus = bonus
        self.contracts_landed = contracts_landed

    def get_pay(self):
        contract_pay = self.base_pay

        if self.contract_type == 'hourly':
            contract_pay = self.hours_worked * self.base_pay

        commission_pay = 0
        if self.commission_rate > 0:
            if self.contract_type == 'salary' and self.contracts_landed > 0:
                commission_pay = self.contracts_landed * self.commission_rate
            elif self.contract_type == 'hourly':
                commission_pay = self.contracts_landed * self.commission_rate

        total_pay = contract_pay + commission_pay + self.bonus
        return total_pay

    def __str__(self):
        if self.contract_type == 'salary':
            contract_info = f"{self.name} works on a monthly salary of {self.base_pay}."
        else:
            contract_info = f"{self.name} works on a contract of {self.hours_worked} hours at {self.base_pay}/hour."

        commission_info = ""
        if self.commission_rate > 0:
            if self.bonus > 0:
                commission_info = f" and receives a bonus commission of {self.bonus}."
            else:
                commission_info = f" and receives a commission for {self.contracts_landed} contract(s) at {self.commission_rate}/contract."

        return f"{contract_info}{commission_info}  Their total pay is {self.get_pay()}."


billie = Employee("Billie", "salary", 4000)
charlie = Employee("Charlie", "hourly", 25, 100)
renee = Employee("Renee", "salary", 3000, contracts_landed=4, commission_rate=200)
jan = Employee("Jan", "hourly", 25, 150, contracts_landed=3, commission_rate=220)
robbie = Employee("Robbie", "salary", 2000, bonus=1500)
ariel = Employee("Ariel", "hourly", 30, 120, bonus=600)