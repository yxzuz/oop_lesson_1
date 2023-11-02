
# What classes should we have
# For each class,
# What are: 1) the data 2) the methods (functions)
class AccountDB:
    def __init__(self):
        self.account_database = []

    def insert(self, account):
        # the original one is create_account in procedural one
        index = self.__search_private(account.account_number)
        if index == -1:
            self.account_database.append(account)
        else:
            print(account, "Duplicated account; nothing to be insert")

    def delete_account(self,num):
        index = self.__search_private(num)
        if index != -1:
            print("Deleting account:", self.account_database[index])
            print('delete was succesful')
            del self.account_database[index]

        else:
            print(num, "invalid account number; nothing to be deleted.")

    def __search_private(self, account_num):
        for i in range(len(self.account_database)):
            if self.account_database[i].account_number == account_num:
                return i
        return -1  # nothing was found in database

    def search_public(self, account_num):
        for account in self.account_database:
            if account.account_number == account_num:
                return account
        return None

    def __str__(self):
        s = ''
        for account in self.account_database:
            s += str(account) + ", "
        return s


class Account:
    def __init__(self, num, type, account_name, balance):
        self.account_number = num
        self.type = type
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        # add money to account
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:  # check whether the money is sufficient
            self.balance -= amount

    def __str__(self):
        return '{' + str(self.account_number) + ',' + str(self.type) + ',' + str(self.account_name) + ',' + str(
            self.balance) + '}'


account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)
account3 = Account("0003", "saving", "Mark Hill", 3000)
account4 = Account("0004", "saving", "David Wood", 4000)
account5 = Account("0004", "saving", "David Wood", 4000)
my_account_DB = AccountDB()
my_account_DB.insert(account1)
my_account_DB.insert(account2)
my_account_DB.insert(account3)
my_account_DB.insert(account4)
my_account_DB.insert(account5)
print(my_account_DB)
# my_account_DB.search_public("0003").deposit(50)  # search if it existed then deposit
# print(my_account_DB)
# my_account_DB.search_public("0003").withdraw(100)
# print(my_account_DB)
#
# my_account_DB.search_public("0003").withdraw(25)
# print(my_account_DB)
my_account_DB.delete_account('0003')
print(my_account_DB)
# show_account('0003')
# deposit('0003', 50)
# withdraw('0001', 6000)
