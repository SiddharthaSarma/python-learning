class User:
    def __init__(self, username='Siddhartha'):
        self.username = username

    def getusername(self):
        return self.username


def main():
    demo = User()
    print(demo.getusername())
    demouser = User('Siddu')
    print(demouser.getusername())

main()
