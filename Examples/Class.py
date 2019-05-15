from enum import Enum, unique

# Make sure the values are unique
# @unique
class Letters(Enum):
    A = 1
    B = 2
    C = 3

class A:
    n = 3
    def __init__(self,n):
        n = n

class Person():
    def __init__(self):
        self.fname = "Robin"
        self.lname = "Cernin"
        self.age = 29
    def __repr__(self):
        return "<Person Class - fname:{0}, lname:{1}, age:{2}".format(
            self.fname, self.lname, self.age
        )
    def __str__(self):
        return "Person ({0} {1} is {2})".format(
            self.fname, self.lname, self.age
        )
    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(
            self.fname, self.lname, self.age
        )
        return bytes(val.encode('utf-8'))
    def __getattr__(self, attr):
        if attr == "name":
            return "{0} {1}".format(self.fname, self.lname)
        else:
            raise AttributeError
    def __setattr__(self, attr, val):
        if attr == "name":
            self.fname = val[0]
            self.lname = val[1]
            self.age = val[2]
        else:
            super().__setattr__(attr, val)
    def __dir__(self):
        return("fname", "lname", "age", "name")

a = A(5)
print(a.n)

print(Letters.A)
print(type(Letters.A))
print(repr(Letters.A))

print(Letters.A.name, Letters.A.value)

person = Person()
print(repr(person))
print(str(person))
print("Format {0}".format(person))
print(bytes(person))
print(person.name)
person.name = ("John", "Doe", 35)
print(person.name)
print(dir(person))