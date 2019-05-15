import collections
import string
from collections import defaultdict
from collections import Counter
from collections import OrderedDict

Point = collections.namedtuple("Point", "x y")
p1 = Point(10, 20)
p2 = Point(30, 40)
print(p1, p2)
print(p1.x, p2.y)

# replace p1 x with 50
p1 = p1._replace(x=50)
print(p1)


letters = ['r','e','e','d','h','a','t']
letters2 = ['a','e','i','o','u']

dictionary = {}

for letter in letters:
    if letter in dictionary.keys():
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1

print(dictionary)

# dictionary = defaultdict(lambda: 0)
dictionary = defaultdict(int)

for letter in letters:
    dictionary[letter] += 1

print(dictionary)

l1 = Counter(letters)
print(l1["e"])
print("There are %d items." % sum(l1.values()))
l1.update(letters2)
print(l1)
print(l1.most_common(3))
l1.subtract(letters)
print(l1)

# Teams with the number of wins and losses

teams = [("Dragons", (20, 20)), ("Broncos", (30, 10)), ("Greens", (5, 35))]
sortedteams = sorted(teams, key=lambda t: t[1][0], reverse=True)
print(sortedteams)
team = OrderedDict(sortedteams)
print(team)

teams, winloss = team.popitem(False)

print(teams, winloss)

for i, teams in enumerate(team, start=1):
    print(i, teams)

a = OrderedDict({'a':1, 'b': 2, 'c': 3})
b = {'a':1, 'c': 3, 'b': 2}
c = OrderedDict({'a':1, 'c': 3, 'b': 2})
print(a == b)
print(a == c)

d = collections.deque(string.ascii_lowercase)
print(d)
d.pop()
d.popleft()
d.append(1)
d.appendleft(2)
print(d)
d.rotate(1)
print(d)