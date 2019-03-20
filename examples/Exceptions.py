
name = "John"
age = 19

try:
    print('Hello ' + str(name) + ', your age is ' + int(age))
except Exception as e:
    print('Exception caught: %s' % e)
