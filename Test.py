# Calculate quadratic formula, ax2+ bx+ c given a,b,c,x
# return can involve a calculation
def quadratic(a, b, c, x):
    first = a * x ** 2
    second = b * x
    third = c
    return first + second + third
