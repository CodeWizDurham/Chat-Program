import bcrypt

class auth:
    def __init__(self, user, passwd):
        self.user = user.encode("utf-8")
        self.passwd = passwd.encode("utf-8")
        self.correct = False
    def setupd(self):
        userw = bcrypt.hashpw(self.user, bcrypt.gensalt())
        passwdw = bcrypt.hashpw(self.passwd, bcrypt.gensalt())
        with open("auth.txt", "a") as authfile:
            authfile.write(f"{userw},{passwdw}\n")
    def login(self):
        with open("auth.txt", "r") as authfile:
            line = authfile.readline()
            userf, passwdf = line.split(",")

#            usef = int(userf)
#            passwdf = int(passwdf)
        if bcrypt.checkpw(self.passwd, passwdf) and bcrypt.checkpw(self.user, userf):
            self.correct = True

auther = auth("User", "Password")
#auther.setupd()
print(auther.login())