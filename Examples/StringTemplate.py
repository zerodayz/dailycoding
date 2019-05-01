from string import Template

name = "John"
age = 29

print("Hello {}, You are {} old.".format(name, age))

template = Template("Hello ${name}, You are ${age} old.")

str1 = template.substitute(name="John", age=29)
print(str1)

data = {
    "name": "John",
    "age": 29
}
str2 = template.substitute(data)
print(str2)