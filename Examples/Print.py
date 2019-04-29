
name = "John"
age = 19

print('Hello %s, your age is %d' % (name, age))
print('Hello %(n)s, your age is %(a)d' % {'n': name, 'a': age})
print('Hello {}, your age is {}'.format(name, age))
print('Hello {n}, your age is {a}'.format(n=name, a=age))
print('Hello ' + str(name) + ', your age is ' + str(age))

print(eval("1+5*3"))

# symbol j for the square root of -1
print(abs(3+4j))
print(abs(1+2j))
# quotient
print(6//4)
# remainder
print(6%4)
print(12%7)
print("{} {}".format(bool([]), bool(None)))
print('hi' if True else 'bye')

print(0**0)
print(0**1)
print(1**0)
print(1**1)

a, b, c = 2,7,8
print(a+b*a)
print(c)
print(16//8)
print(a+(b*a)//c)
print(14//8)