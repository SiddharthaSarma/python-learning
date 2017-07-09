# tuples are immutable objects where as lists are mutable objects
# tuples are indicated by braces() where as lists are indicated by square brackets[]


def main():
    # tuples
    a = (1, 2, 3, 4, 5)
    print(a)

    # lists
    b = [1, 2, 3, 4, 5]
    print(b)

    # looping over lists
    for i in b:
        print(i)
    print()

    # Looping over strings
    string = 'Hello'
    for i in string:
        print(i)
    print()

main()
