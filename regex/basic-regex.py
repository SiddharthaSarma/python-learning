# import regular expression package
import re


def basic_regex():
    fh = open('../assets/doctor-foster.txt')
    for line in fh:
        if re.search('puppy', line):
            print(line)


basic_regex()


