from abc import ABC, abstractmethod

# class Father(ABC):
#     @abstractmethod
#     def disp(self):
#         pass

#     def show(self):
#         print("Hello")

# # f1 = Father()
# class Child(Father):
#     def disp(self):
#         print("Child Class")
        
# c = Child()
# c.show()
# c.disp()

class RBI(ABC):
    @abstractmethod
    def loan_dept(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def internet_banking(self):
        pass

    def m1(self):
        print("Concrete Method")

class ICICI(RBI):
    def loan_dept(self):
        print("Loan")

    @abstractmethod
    def deposit(self):
        print("Deposit")

    @abstractmethod
    def internet_banking(self):
        print("Internet")

a1 = ICICI()
a1.loan_dept()