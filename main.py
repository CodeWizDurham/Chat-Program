import bcrypt


class Auth:
    def __init__(self, user, passwd):
        self.user = user
        self.passwd = passwd.encode('utf-8')
        self.correct = False

    def setupd(self):
        passwdw = bcrypt.hashpw(self.passwd, bcrypt.gensalt()).decode('utf-8')
        with open("auth.txt", "a") as authfile:
            authfile.write(f"{self.user},{passwdw}\n")

    def login(self):
        with open("auth.txt", "r") as authfile:
            for line in authfile:
                userf, passwd = line.split(",")
                passwd = passwd.encode('utf-8')
                if userf == self.user:
                    self.correct = bcrypt.checkpw(self.passwd, passwd)