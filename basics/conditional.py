def main():
    a, b = 0, 1
    if a < b:
        print("a is less than b")
    elif a > b:
        print('a is less than b')
    else:
        print("a is equal to b")

main()


def inlinecondition():
    a, b = 0, 1
    print("Hello" if a < b else "Hello world")

inlinecondition()

