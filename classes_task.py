import datetime 


#classes--------------------------------

class Employee:
	def __init__(self,name,age,salary,employment_year, **kwargs):
		self.name = name.capitalize()
		self.age = age
		self.salary = int(salary)
		self.employment_year = int(employment_year)

		for key, value in kwargs.items():
			setattr(self, key, value)

	def get_working_years(self):
		return int(datetime.datetime.today().year) - self.employment_year

	def __str__(self):
		return "name: {}, age: {}, salary: {}, working years: {}".format(self.name, self.age, self.salary, self.get_working_years())


#----------------------------

class Manager (Employee):
	def __init__(self, name,age,salary,employment_year, bonus_percentage, **kwargs):
		super().__init__(name, age,salary, employment_year, **kwargs)
		self.bonus_percentage = float(bonus_percentage)

	def get_bonus(self):
		return self.bonus_percentage * self.salary

	def __str__(self):
		return super().__str__() + ", bonus: {}".format(self.get_bonus())


#MAIN - - - - - - - - - - - - - - - - - - -
def print_list(list):
	for item in list:
			print(item)
			print("")


employees = []
managers = []


print("Welcome to HR Pro 2019")

while True:
	

	print("""Choose an action to do:
        1. show employees
        2. show managers
        3. add an employee
        4. add a manager
        5. exit""")
	choice = int(input("What would you like to do?  "))
	if choice == 1:
		print("Employees: ")
		print_list(employees)

	elif choice == 2:
		print("Managers: ")
		print_list(managers)

	elif choice == 3:

		employee_name = input("Enter name:  ")
		employee_age = input("Enter age:  ")
		employee_salary = input("Enter salary:  ")
		employee_date = input("Enter employment date:  ")
		employees.append(Employee(employee_name, employee_age, employee_salary, employee_date))
		
		print("Employee added succesfully\n")

	elif choice == 4:

		employee_name = input("Enter name:  ")
		employee_age = input("Enter age:  ")
		employee_salary = input("Enter salary:  ")
		employee_date = input("Enter employment date:  ")
		manager_bonus = input("Enter manager bonus percentage:  ")
		managers.append(Manager(employee_name, employee_age, employee_salary, employee_date, manager_bonus))
		
		print("Manager added succesfully\n")

	elif choice == 5:
		break

	else:
		print("Error invalid choice")
