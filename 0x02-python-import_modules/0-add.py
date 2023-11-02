#!/usr/bin/python3
if __name__ == '__main__':
    from add_0 import add
    a = 1
    b = 2
# Calculate the result using the imported module
result = add(a, b)

# Print the result
print("{:d} + {:d} = {:d}".format(a, b, result))
