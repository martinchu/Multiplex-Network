#usr/bin/python
import tensorflow as tf
import numpy as np
import random as rand

class Bank(object):

    BankTotal = 0
    def BngetRand(range0, range1):
        return rand.uniform(range0, range1);
    def __init__(self):
        # banks[i]["fixed_income_exposure"] = getRand(0.35,0.6)*(10**9);
        self.fixed_income_exposure = rand.uniform(0.35, 0.6)*(10**9)
        # banks[i]["derivatives_exposure"] = getRand(0, 0.3)*(10**9);
        self.derivatives_exposure = rand.uniform(0, 0.3)*(10**9)
        # banks[i]["securities_financing_exposure"] = getRand(0.65, 0.9)*(10**9);
        self.securities_financing_exposure = rand.uniform(0.65, 0.9)*(10**9)
        self.sum_exposures = self.securities_financing_exposure + self.derivatives_exposure + self.fixed_income_exposure
        # ten_pc_exp = 0.1*banks[i]["sum_exposures"]
        # fifteen_pc_exp = 0.15*banks[i]["sum_exposures"]
        # banks[i]["min_cap"] = getRand(ten_pc_exp, fifteen_pc_exp)
        self.min_cap = rand.uniform(self.sum_exposures*0.1,self.sum_exposures*0.15)

    def __str__(self):
        print "Fixed Income Exposure: {}:".format(self.fixed_income_exposure)
        print "Derivatives Exposure: {}".format(self.derivatives_exposure)
        print "Securities Exposure: {}".format(self.securities_financing_exposure)
        print "Sum Exposures: {}".format(self.sum_exposures)
        print "Minimum Exposures: {}".format(self.min_cap)
        return "======="

    def availableFund(self):
        return self.capital - self.minCapital

    def updateCapital(self, exposure):
        self.capital -= exposure
