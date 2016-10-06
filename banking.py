class BankAccount(object):
    balance = 0
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return ("This account belongs to %s and the balance is $%.2f") % (self.name, self.balance)

    def show_balance(self):
        print "Your balance is $%.2f" % self.balance

    def deposit(self, amount):
        if amount <= 0:
            print "Invalid entry."
            return
        else:
            print "You have chosen to deposit $%.2f." % (amount)
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if amount >= self.balance:
            print "Invalid entry. You may not overdraw your balance at this time."
            return
        else:
            print "You have chosen to withdraw $%.2f." % amount
            self.balance -= amount
            self.show_balance()

my_account = BankAccount("rachael")
print my_account
my_account.show_balance()
my_account.deposit(2000)
print my_account
my_account.withdraw(1000)
print my_account
