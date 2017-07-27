def read_file():
    fh = open('doctor-foster.txt', 'r')
    for line in fh:
        print(line)
    fh.close()


read_file()


def write_file():
    total_amount = 100
    with open("Output.txt", "w") as text_file:
        print("Purchase Amount: {}".format(total_amount), file=text_file)


write_file()
