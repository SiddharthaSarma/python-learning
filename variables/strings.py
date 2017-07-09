# strings can be wrapped in double quotes("") or single quotes('')
# triple single quotes or double quotes can be used to print multiple lines


def logmessage(message=''):
    print()
    print('********************************')
    print('       '+message+'          ')
    print('********************************')

logmessage('Strings')


def main():
    basicstring = 'Hello world!'
    print(basicstring)

    logmessage("Escape characters")
    escapestring = 'Hello \nworld!'
    print(escapestring)

    logmessage('Raw string')
    rawstring = r'Hello \nworld!'
    print(rawstring)

    logmessage('String concat')
    # python 3 way
    a = 'hello world'
    string = 'This is {}'.format(a)
    print(string)

    # python 2 way
    string = 'This is %s' %a
    print(string)

    logmessage('Multiple lines')
    string = '''\
Hello this is siddhartha
My age is 23 years
I am working in hyderabad
    '''
    print(string)


main()
