def read_file():
    fh = open('doctor-foster.txt', 'r');
    for line in fh:
        print(line)
    fh.close()


read_file()
