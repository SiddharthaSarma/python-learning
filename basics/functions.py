# Function with no parameters
def loop():
    for i in range(10):
        print(i, end=" ")
    print()
loop()


# Function with no parameters
def functionwithparameters(a):
    for i in range(a, 10):
        print(i, end=" ")
    print()

functionwithparameters(5)


# Function with default parameters
def defaultparamfunction(a=5):
    for i in range(a, 10):
        print(i, end=" ")
    print()

defaultparamfunction()

