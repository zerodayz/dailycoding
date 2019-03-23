# Fibonacci Sequence #1


def get_fib(position):

    print("get_fib(%s)" % position)
    if position == 0:
        return 0
    elif position == 1:
        return 1
    first = 0
    second = 1
    next = first + second

    for i in range(2, position):
        first = second
        second = next
        next = first + second
        i += 1
    return next

# Fibonacci Sequence #2


def get_fib_list(position):

    print("get_fib_list(%s)" % position)
    fib_seq = []

    for c in range(0, position + 1):
        if c == 0:
            fib_seq.append(0)
        elif c == 1:
            fib_seq.append(1)
        elif c >= 2:
            fib_seq.append(fib_seq[c-2] + fib_seq[c-1])

    return fib_seq


# Fibonacci Sequence Recursive


def get_fib_recursive(position):

    if position < 2:
        return position
    else:
        return get_fib_recursive(position - 2) + get_fib_recursive(position - 1)

# Test cases
n = 8
print(get_fib(n))
print(get_fib_list(n))
print("get_fib_recursive(%s)" % n)
print(get_fib_recursive(n))
