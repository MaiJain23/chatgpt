listA=[1,2,3,4,5,6]
firstname ="mayuri"

class Person:
    firstName = None
    lastName = None

    def displayName(self):
        print(self.firstName +" " +self.lastName)

amol = Person()
print(amol.firstName)
print(amol.lastName)
#amol.displayName()

amol.firstName = "amol"
amol.lastName = "kalegore"
print(amol.firstName)
print(amol.lastName)
amol.displayName()

atul = Person()
print(atul.firstName)
print(atul.lastName)
#atul.displayName()
atul.firstName = "atul"
atul.lastName = "kalegore"
atul.language = "marathi"
print(atul.firstName)

#program 2 

class Person2():
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln

    def displayName(self):
        print(self.firstname + self.lastname)
ridhima = Person2("ridhima","kalegore")
ridhima.displayName()

rakhi = Person2("rakhi","kaulkar")
rakhi.displayName()

class Bank():
    country = "india"
    def __init__(self,fn,ln,accNo,bal):
        self.firstName = fn
        self.lastName = ln
        self.accountNUm = accNo
        self.balance = bal

    def deposite(self,amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdrawl(self,amount):
        if amount < self.balance:
            self.balance = self.balance - amount
        else:
            print("insufficient balance")

atul = Bank("atul","kalegore",123,100000)
print(atul.firstName)
print(atul.lastName)
print(atul.country)
print(atul.accountNUm)
print(atul.balance)

atul.withdrawl(200000)
atul.deposite(100000)
print(atul.balance)
