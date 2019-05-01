RED='\033[91m'
GREEN='\033[92m'
WHITE='\033[0m'

print(RED, "False", WHITE,"   =>", False)
print(GREEN, "True", WHITE,"    =>", True)
print(RED, "False", WHITE,"   and   ",RED, "False", WHITE,"   =>", False and False)
print(RED, "False", WHITE,"   and   ",GREEN, "True", WHITE,"    =>", False and True)
print(RED, "False", WHITE,"   or    ",RED, "False", WHITE,"   =>", False or False)
print(RED, "False", WHITE,"   or    ",GREEN, "True", WHITE,"    =>", False or True)

print(GREEN, "True", WHITE,"    and   ",GREEN, "True", WHITE,"    and    ",GREEN, "True", WHITE,"    =>", True and True and True)
print(GREEN, "True", WHITE,"    and   ",RED, "False", WHITE,"   and    ",GREEN, "True", WHITE,"    =>", True and False and True)
print(GREEN, "True", WHITE,"    and   ",RED, "False", WHITE,"   and    ",RED, "False", WHITE,"   =>", True and False and False)
print(RED, "False", WHITE,"   and   ",RED, "False", WHITE,"   and    ",RED, "False", WHITE,"   =>", False and False and False)
print(RED, "False", WHITE,"   or    ",RED, "False", WHITE,"   or     ",RED, "False", WHITE,"   =>", False or False or False)
print(RED, "False", WHITE,"   or    ",GREEN, "True", WHITE,"    or     ",RED, "False", WHITE,"   =>", False or True or False)
print(RED, "False", WHITE,"   or    ",GREEN, "True", WHITE,"    or     ",GREEN, "True", WHITE,"    =>", False or True or True)
print(GREEN, "True", WHITE,"    or    ",GREEN, "True", WHITE,"    or     ",GREEN, "True", WHITE,"    =>", False or True or True)
print(GREEN, "True", WHITE,"    and   ",GREEN, "True", WHITE,"    or     ",GREEN, "True", WHITE,"    =>", True and True or True)
print(GREEN, "True", WHITE,"    and   ",RED, "False", WHITE,"   or     ",GREEN, "True", WHITE,"    =>", True and False or True)
print(GREEN, "True", WHITE,"    and   ",RED, "False", WHITE,"   or     ",RED, "False", WHITE,"   =>", True and False or False)
print(RED, "False", WHITE,"   and   ",RED, "False", WHITE,"   or     ",RED, "False", WHITE,"   =>", False and False or False)
print(GREEN, "True", WHITE,"    or    ",GREEN, "True", WHITE,"    and    ",GREEN, "True", WHITE,"    =>", True or True and True)
print(GREEN, "True", WHITE,"    or    ",RED, "False", WHITE,"   and    ",GREEN, "True", WHITE,"    =>", True or False and True)
print(GREEN, "True", WHITE,"    or    ",RED, "False", WHITE,"   and    ",RED, "False", WHITE,"   =>", True or False and False)
print(RED, "False", WHITE,"   or    ",RED, "False", WHITE,"   and    ",RED, "False", WHITE,"   =>", False or False and False)