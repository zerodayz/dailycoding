# We iterate over every manatee in the manatees list with the for loop.
# Since we're given that manatees has n elements, our code will take approximately O(n) time to run.
# O(n)

def example1(manatees):
    for manatee in manatees:
        print manatee['name']

# We look at two specific properties of a specific manatee.
# We aren't iterating over anything - just doing constant-time lookups on lists and dictionaries.
# Thus the code will complete in constant, or O(1), time.
# O(1)

def example2(manatees):
    print manatees[0]['name']
    print manatees[0]['age']

# There are two for loops, and nested for loops are a good sign that you need to multiply two runtimes.
# Here, for every manatee, we check every property. If we had 4 manatees, each with 5 properties,
# then we would need 5+5+5+5 steps.
# This logic simplifies to the number of manatees times the number of properties, or O(nm).
# O(nm)

def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print manatee_property, ": ", manatee[manatee_property]

# Again we have nested for loops.
# This time we're iterating over the manatees list twice - every time we see a manatee,
# we compare it to every other manatee's age. We end up with O(nn), or O(n^2) (which is read as "n squared").
# O(n^2)

def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print oldest_manatee

# For reference: http://bigocheatsheet.com/
# https://wiki.python.org/moin/TimeComplexity