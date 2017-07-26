def main():
    a, b = 0, 1
    if a < b:  # No need of extra parenthesis
        print('a is less than b')
    else:
        print('b is less than a')

main()


def checkoddnumber(number):
    if number % 2 > 0:
        print('Weird')
    elif 2 <= number <= 5:
        print('Not Weird')
    elif 6 <= number <= 20:
        print('Weird')
    else:
        print('Not Weird')

checkoddnumber(8)
