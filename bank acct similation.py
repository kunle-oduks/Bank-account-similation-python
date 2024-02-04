
class Account: #Create class

#init method as constructor and assign values to attributes
  def __init__(self, account_number, account_balance, account_holder):
    self.account_number = account_number
    self._account_balance = account_balance #( _ is added to attribute to protect from direct access
    self.account_holder = account_holder

  def deposit(self, amt_deposited): #(function) amount deposited is added to balance and new balance returned
    print(f"Acct No:{self.account_number[0:3]}****{self.account_number[-3:]}")
    print(f"Credit Alert:  NGN{amt_deposited:,.2f}" )
    self._account_balance += amt_deposited
    return f"Your balance is NGN{self._account_balance:,.2f}"

  def withdraw(self, amt_withdrawn):#(function(amt withdrawn is deducted from balance and new balance returned)
    if self._account_balance >= amt_withdrawn: #Check to prevent account from being overdrawn
       print(f"Acct No:{self.account_number[0:3]}****{self.account_number[-3:]}")
       print(f"Debit Alert:  NGN{amt_withdrawn:,.2f}" )
       self._account_balance -= amt_withdrawn
       return f"Your balance is NGN{self._account_balance:,.2f}"
    
    else: #unfunded account response
      print(f"Acct No:{self.account_number[0:3]}****{self.account_number[-3:]}")
      print("You do not have sufficient balance for this withdrawal")
      return f"Your current balance is NGN{self._account_balance:,.2f}"

  def check_balance(self): #function to check balance 
    print(f"Acct No:{self.account_number[0:3]}****{self.account_number[-3:]}")
    return f"Your balance is NGN{self._account_balance:,.2f}"

#Account number generator to prevent duplication
num_DB = []
acct_num = 1000000000
for i in range(1, 1000000):
  acct_num += 1
  num_DB.append(acct_num)

#creation of instances of the Account class object
my_account1 = Account(str(num_DB[0]), 1000.00, "Kunle Odukoya")
my_account2 = Account(str(num_DB[1]), 680.12, "Kazeem Obitunde")
my_account3 = Account(str(num_DB[2]), 1005467.67, "Kemi Odunowo")
my_account4 = Account(str(num_DB[3]), 4888.20, "Joseph Yobo")
my_account5 = Account(str(num_DB[4]), 657123.35, "Victor Nwaifo")

#Test run of functions and attributes using above created instances of the Account class
print(my_account1.deposit(100.00)+"\n")
print(my_account1.withdraw(1300.00)+"\n")
print(my_account1.check_balance()+"\n")
print(my_account2.deposit(61000.32)+"\n")
print(my_account2.check_balance()+"\n")
print(my_account2.withdraw(50450.75)+"\n")
print(my_account3.withdraw(2000.00)+"\n")
print(my_account3.deposit(8000.00)+"\n")
print(my_account3.check_balance()+"\n")
print(my_account4.check_balance()+"\n")
print(my_account4.withdraw(2000.00)+"\n")
print(my_account4.deposit(6000.32)+"\n")
print(my_account5.check_balance()+"\n")
print(my_account5.withdraw(1000000.00)+"\n")
print(my_account5.withdraw(50000.67)+"\n")




