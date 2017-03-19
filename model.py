class Bank(object):

    BankTotal = 0

    def __init__(self, c, mc):
        self.capital = c
        self.minCapital = mc
        BankTotal++;

    def __str__(self):
        print "Bank Capital: {} \nMinimum Capital: {} ".format(self.capital, self.minCapital)

    def availableFund(self):
        return self.capital - self.minCapital

    def updateCapital(self, exposure):
        self.capital -= exposure
