
name = "John"
age = 19

print('Hello %s, your age is %d' % (name, age))
print('Hello %(n)s, your age is %(a)d' % {'n': name, 'a': age})
print('Hello {}, your age is {}'.format(name, age))
print('Hello {n}, your age is {a}'.format(n=name, a=age))
print('Hello ' + str(name) + ', your age is ' + str(age))

print(eval("1+5*3"))
print("{} {}".format(bool([]), bool(None)))