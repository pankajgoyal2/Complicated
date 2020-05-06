class employ:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = fname + lname + '@gmail.com'
    def full_name(self):
        return self.fname + self.lname
