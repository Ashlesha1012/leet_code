####################################################################

# b = 10
# class A:
#     stat_var = 10
#     def __init__(self, v1):
#         self.__Name = v1

#     def __get_name(self):
#         print(self.__Name)

#     def get_name(self):
#         self.__get_name()
#         return "Aa"
    
# class B(A):
#     def __init__(self, v2):
#         super().__init__(v2)

# b1 = B('ABC')
# print(b1._A__Name)      # Output:ABC (name_mangling)
# # print(b1.Name)          # AttributeError: 'B' object has no attribute 'Name'
# # print(b1.__Name)          # AttributeError: 'B' object has no attribute '__Name'
# # b1.__get_name()            # AttributeError: 'B' object has no attribute '__get_name'
# # b1._A__get_name()        # ABC
# print(b1.get_name())

####################################################################

# class Base:
#     def __init__(self):
#         self._a = 2

# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#         print("Calling protected member of base class: ", self._a)
#         self._a = 3
#         print("Calling modified protected member: ", self._a)

# s1 = Base()
# print("Accessing protected member of Base class object", s1._a)    # Accessing protected member of Base class object 2
# s2 = Derived()
# print("Accessing protected member of Derived class object",s2._a)    

####################################################################

# class Base:
#     def __init__(self):
#         self._a = 2

# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print(self._a)
#         self._a = 3
#         print(self._a)

# s1 = Base()
# print(s1._a)
# s2 = Derived()
# print(s2._a)

####################################################################

class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print(self.__c)

# obj = Base()
# print(obj.a)
# print(obj._Base__c)
# d = Derived()

####################################################################

class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value
    
    @value.deleter
    def value(self):
        del self._value

obj = MyClass(42)
print(obj.value)
obj.value = 100
print(obj.value)
del obj.value
print(obj.value)