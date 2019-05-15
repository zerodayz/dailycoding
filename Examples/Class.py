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