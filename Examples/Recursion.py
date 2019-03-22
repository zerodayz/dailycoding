def recursive(input):
    print("recursive(%s)" %input)
    if input <= 0:
        print("returning 0 into output")
        return input
    else:
        print("entering recursive(%s)" %( input -1 ))
        output = recursive(input -1)
        print("output = %s from recursive(%s)" %(output, input - 1))
        return output

print(recursive(3))