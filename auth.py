from passlib.hash import bcrypt

class auth:
    def __init__(self, user, passwd, setup):
        self.hasher = bcrypt.using()
        self.user = user
        self.passwd = passwd
        self.setup = setup
        self.correct = False
    def setupd(self):
        userw = self.hasher.hash(self.user)
        passwdw = self.hasher.hash(self.passwd)
        with open("auth.txt", "a") as authfile:
            authfile.write(f"{userw},{passwdw}\n")
    def login(self):
        with open("auth.txt", "r") as authfile:
            line = authfile.readline()
            userf, passwdf = line.split(",")
        if self.hasher.verify(self.user, userf) and self.hasher.verify(self.passwd, passwdf):
            self.correct = True
            return self.correct
auther = auth("User", "Password", False)
print(auther.login())