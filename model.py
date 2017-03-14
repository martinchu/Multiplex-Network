class Bank(object):

    def __init__(self, c, mc):
        self.capital = c
        self.minCapital = mc

    def print_capital(self):
        print "Bank Capital: {} \nMinimum Capital: {} ".format(self.capital, self.minCapital)
