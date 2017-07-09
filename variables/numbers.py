def logmessage(message=''):
    print()
    print('********************************')
    print('       '+message+'          ')
    print('********************************')

logmessage('Numbers')


def main():
    a = 52
    b = 52.0
    print("Type of a", type(a))
    print("Type of b", type(b))
    c = a / 9  # outputs 5.7777
    print("c value is ", c)
    d = a // 9  # outputs 5
    print("d value is ", d)
    e = a % 9  # outputs remainder
    print("e value is ", e)

main()

logmessage('Rounding values')


# Using round to truncate the values
def roundvalues():
    a, b = 52, 9
    c = round(a/b)
    print("Round value is ", c)
    d = round(a/b, 2)
    print("Rounded value by arguments", d)

roundvalues()

logmessage('Type conversion')


# Using type conversion
def typeconversion():
    a, b = 52, 9
    c = a/b
    print("c value without type conversion", c)
    d = int(a/b)
    print("After type conversion to int", d)
    e = float(a/b)
    print("After type conversion to float", e)

typeconversion()

