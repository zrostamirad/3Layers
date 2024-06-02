class setting():

    def GetConnectionString(self):
        with open("constr.txt") as f:
            return str(f.read())
