import time



class person:
    def __init__(self, age, name, adress, **kwargs ):
        super().__init__(**kwargs) 
        print(f"Initializing Person: {name}")
        self.name=name
        self.age=age
        self.adress=adress

        
    def get_details(self):
        return [self.name, self.age, self.adress]
    
class customer(person):
    def __init__(self, age, name, adress, customer_id, **kwargs):
        # Fix: Pass the arguments you captured to the super() call
        super().__init__(age=age, name=name, adress=adress, **kwargs) 
        
        print(f"Initializing Customer: {customer_id}")
        self.customer_id=customer_id
        self.accounts = {}
    
    # ... rest of the methods
    def open_account(self, account_type, initial_deposit, account_number, interest_rate=0):
        if account_type == 'savings':  # <-- Fix: 'saving' -> 'savings'
            new_account = SavingsAccount(account_number, initial_deposit, interest_rate)
            self.accounts[account_number] = new_account
            print(f"Savings Account {account_number} created for {self.name}.") # Use self.name
        elif account_type == 'current':
            # Note: You named this CurrentAccount, not CheckingAccount
            new_account = CurrentAccount(account_number, initial_deposit) 
            self.accounts[account_number] = new_account
            print(f"Current Account {account_number} created for {self.name}.") # <-- Fix: Print "Current"
        else:
            print('Please enter correct acc type.')
            return

class employee(person):
    def __init__(self, employee_id, salary, **kwargs):
        super().__init__(**kwargs)
        print(f'Init Employee: {employee_id}')
        self.employee_id=employee_id
        self.salary=salary
    def do_work(self):
        print(f'Employee: {self.name}({self.employee_id}) is working.')


class account:
    def __init__(self, accountnumber, balance):
        self.account_number=accountnumber
        self.balance=balance
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f'depositd {amount}. Now balance= {self.balance}')
        else:
            print('Please enter correct amount')

    def withdraw(self, amount):
        if amount>self.balance:
            print(f'Insufficient balance! \nAvailable balance: rs.{self.balance}')
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else :
            self.balance-=amount
            print(f'withdraw rs{amount}, New balance: {self.balance}')
    def get_balance(self):
        return self.balance

class SavingsAccount(account):
    def __init__(self, accountnumber, balance, interest_rate):
        super().__init__(accountnumber, balance)
        self.InterestRate=interest_rate

    def calculate_interest(self):
        pass


class CurrentAccount(account):
    def __init__(self, accountnumber, balance):
        super().__init__(accountnumber, balance)

    def overdraft_limit(self):
        pass


        
class BankManager(employee, customer):
    def __init__(self, name, age, adress, customer_id, employee_id, salary, manager_level):
        print("\n--- Creating BankManager ---")
        super().__init__(
            name=name,
            age=age,
            adress=adress,
            customer_id=customer_id,
            employee_id=employee_id,  # <-- THIS WAS MISSING
            salary=salary
        )

        self.manager_level = manager_level  # <-- Fix typo: 'manager_lavel'
        print(f"Initializing Manager (Level {self.manager_level})")
        print("--- BankManager Created ---")
    
    # ... rest of the methods

    def approve_loan(self):
        print(f"Manager {self.name} approves the loan.")







# (Account classes would be defined up here)
# (Person, Customer, Employee classes defined up here)
# (BankManager class defined up here)
# --- ROADMAP STEP 4: THE BANK CONTROLLER ---

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = {}  # Store customer objects, maybe use customer_id as key?
        self.employees = {}  # Store employee objects, maybe use employee_id as key?
        print(f"Welcome to {self.bank_name}!")

    def register_customer(self, name, age, adress, customer_id):
        """
        Creates a new customer object and stores it in self.customers
        """
        if customer_id in self.customers:
            print(f"Error: Customer ID {customer_id} already exists.")
            return None
        
        new_customer = customer(age=age, name=name, adress=adress, customer_id=customer_id)
        self.customers[customer_id] = new_customer
        print(f"Customer {name} registered with ID {customer_id}.")
        return new_customer

    def hire_manager(self, name, age, adress, customer_id, employee_id, salary, manager_level):
        """
        Creates a new BankManager object and stores it in self.employees
        """
        if employee_id in self.employees:
            print(f"Error: Employee ID {employee_id} already exists.")
            return None
        
        # Note: A manager is ALSO a customer. We should add them to both lists!
        new_manager = BankManager(
            name=name, age=age, adress=adress, 
            customer_id=customer_id, employee_id=employee_id, 
            salary=salary, manager_level=manager_level
        )
        
        self.employees[employee_id] = new_manager
        
        # Also register them as a customer if their ID is unique
        if customer_id not in self.customers:
            self.customers[customer_id] = new_manager
        
        print(f"Manager {name} hired with Employee ID {employee_id}.")
        return new_manager

    def find_customer(self, customer_id):
        """
        Finds and returns a customer object from self.customers
        """
        return self.customers.get(customer_id, None)

    def find_employee(self, employee_id):
        """
        Finds and returns an employee object from self.employees
        """
        return self.employees.get(employee_id, None)

# --- NEW TEST SCRIPT (STEP 5) ---

print("--- Initializing Bank System ---")
my_bank = Bank(bank_name="Python National Bank")

print("\n--- Hiring and Registering ---")
manager = my_bank.hire_manager(
    name="Jane Doe", age=45, adress="123 Bank St", 
    customer_id="C-001", employee_id="E-001", 
    salary=90000, manager_level=5
)

cust1 = my_bank.register_customer(
    name="John Smith", age=30, adress="456 Main St", customer_id="C-002"
)

print("\n--- Performing Bank Operations ---")

# Find a customer and open an account
customer_to_find = my_bank.find_customer("C-002")
if customer_to_find:
    customer_to_find.open_account("savings", 1000, "S-101", 0.02)
    customer_to_find.accounts["S-101"].deposit(250)
    
# Use the manager's employee AND customer abilities
manager_as_employee = my_bank.find_employee("E-001")
manager_as_employee.do_work()
manager_as_employee.approve_loan()

manager_as_customer = my_bank.find_customer("C-001")
manager_as_customer.open_account("current", 10000, "M-101")
manager_as_customer.accounts["M-101"].withdraw(500)