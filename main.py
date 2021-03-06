#! /usr/bin/python
import tensorflow as tf
import numpy as np
import random as rand
from model import Bank

failedSet = set()
bankList = []

def main():
    # Step 0: Read in Input
    # inputSead = open('sample.in', 'w')
    # inputSead.read()

    # banks =  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22];
    # banks = [1, 2, 3, 4, 5, 6]
    # mcMatrix = [7, 8, 9, 10, 11]
    # cMatrix = [12, 13, 14, 15, 16]
    # # Will Change into more realistic numbers
    # numBank = len(banks)
    # # Step 1: set bank objects
    # for k in range(0, numBank-1):
    #     b = Bank(cMatrix[k], mcMatrix[k])
    #     BankList.append(b)

    # #
    # # for j in range(0, numBank-1):
    # #     print j
    # #     BankList[j].print_capital()

    # # Step 2: Calculate Sead Matrix
    # SeadMatrix = []
    # for a in range(0,numBank -1):
    #     row = []
    #     for b in range(0, numBank -1):
    #         row.append(0)
    #     SeadMatrix.append(row)

    # for i in range(0, numBank - 1):
    #     for j in range(0, numBank - 1):
    #         SeadMatrix[i][j] = eadValues[i]/ BankList[i].capital;
    #         # Calculate SeadValue(ij)
    # # SeadMatrix = [[0.50432, 0.172312, 0.294093, 0.008432, 0.005784, 0.000439, 0.011853, 0.00168, 0.000856, 2.5e-05, 5e-05, 5.2e-05, 2.6e-05, 5e-05, 1.2e-05, 7e-06, 4e-06, 4e-06, 0.0, 0.0, 0.0, 1e-06], [0.670176, 0.248377, 0.048715, 0.028854, 0.001302, 5.7e-05, 0.001353, 0.000883, 1.2e-05, 0.000192, 6.1e-05, 4e-06, 7e-06, 1e-06, 3e-06, 0.0, 0.0, 1e-06, 0.0, 0.0, 0.0, 2e-06], [0.336556, 0.516654, 0.074067, 0.010023, 0.036753, 0.016915, 0.005687, 0.00072, 0.001213, 0.000246, 0.000251, 0.000438, 0.000425, 2.8e-05, 1.7e-05, 1e-06, 2e-06, 2e-06, 0.0, 1e-06, 0.0, 1e-06], [0.531381, 0.110834, 0.179639, 0.099575, 0.064162, 0.012234, 0.001263, 0.000835, 7e-05, 6e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.06966, 0.855981, 0.064811, 0.005858, 0.002526, 0.000343, 0.000652, 0.000117, 4.1e-05, 5e-06, 2e-06, 2e-06, 1e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.524308, 0.400104, 0.009994, 0.041661, 0.003956, 0.014496, 0.00512, 0.000248, 4e-06, 1.2e-05, 0.0, 7.8e-05, 1.7e-05, 1e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.286013, 0.369865, 0.068486, 0.253115, 0.011692, 0.006386, 0.001619, 0.002338, 0.000189, 4.9e-05, 8.8e-05, 5e-05, 2.1e-05, 4.6e-05, 1e-06, 2.8e-05, 1.3e-05, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.193094, 0.782733, 0.010473, 0.008641, 0.00309, 0.000921, 0.000927, 0.000104, 6e-06, 7e-06, 3e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.324137, 0.628859, 0.008015, 0.031321, 0.003073, 0.002771, 0.001385, 0.000302, 9.5e-05, 2e-06, 1.7e-05, 1.9e-05, 3e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.695347, 0.105825, 0.011974, 0.062957, 0.053654, 0.020336, 0.018383, 0.007772, 0.015464, 0.006437, 0.00046, 3.5e-05, 0.000458, 0.000198, 1.2e-05, 0.000472, 6.5e-05, 2.3e-05, 6e-05, 1.1e-05, 6e-06, 5.1e-05], [0.501057, 0.419467, 0.02381, 0.033184, 0.017515, 0.00492, 2.2e-05, 2e-05, 4e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.465971, 0.149014, 0.176249, 0.010132, 0.04543, 0.025582, 0.099116, 0.027326, 0.00112, 2e-06, 2.6e-05, 8e-06, 1.9e-05, 3e-06, 1e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.253633, 0.342635, 0.330257, 0.050229, 0.001168, 0.009867, 0.007212, 0.003135, 0.001018, 0.000525, 6e-05, 0.000254, 5e-06, 1e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.705115, 0.272845, 0.015136, 0.004225, 0.00191, 0.00059, 1.1e-05, 2e-06, 5.2e-05, 1.7e-05, 2.8e-05, 5.9e-05, 0.0, 0.0, 9e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.750994, 0.072589, 0.094032, 0.065306, 0.014865, 0.000342, 0.000338, 0.001017, 0.000374, 5.8e-05, 4.8e-05, 1.5e-05, 4e-06, 3e-06, 1e-06, 5e-06, 7e-06, 1e-06, 0.0, 0.0, 0.0, 1e-06], [0.016015, 0.241717, 0.5384, 0.022019, 0.057027, 0.103143, 0.006044, 0.003137, 0.002717, 0.003788, 0.005475, 0.000126, 0.000247, 9.6e-05, 4.1e-05, 2e-06, 5e-06, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.485445, 0.243538, 0.172077, 0.021574, 0.012556, 0.044642, 0.016183, 0.000539, 0.001911, 0.000286, 3.5e-05, 0.001127, 5e-05, 2.6e-05, 8e-06, 1e-06, 0.0, 0.0, 0.0, 1e-06, 0.0, 1e-06], [0.754962, 0.079916, 0.145107, 0.012521, 0.001569, 0.001262, 0.004193, 0.000343, 2e-05, 6.7e-05, 3.1e-05, 5e-06, 3e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.860901, 0.090599, 0.029231, 0.009017, 2.6e-05, 0.003308, 0.001255, 0.005397, 6.8e-05, 5e-05, 8e-06, 3.2e-05, 3e-06, 3.1e-05, 6e-05, 7e-06, 5e-06, 1e-06, 0.0, 0.0, 0.0, 1e-06], [0.085459, 0.690195, 0.092155, 0.123683, 0.00421, 0.002064, 0.001505, 0.00068, 3.7e-05, 1.1e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.206255, 0.173831, 0.484086, 0.06344, 0.063526, 0.001979, 0.00532, 0.001308, 0.000233, 2e-06, 5e-06, 1.3e-05, 1e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-06], [0.186563, 0.554057, 0.044766, 0.062073, 0.016857, 0.103566, 0.007748, 0.02129, 0.00217, 0.000581, 8.7e-05, 0.000139, 2.2e-05, 4.2e-05, 3.6e-05, 2e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-06]]
    # eadValues = [-0.50432, 0.172312, -0.294093, 0.008432, 0.005784, 0.000439, 0.011853, 0.00168, -0.000856, 2.5e-05, 5e-05, -5.2e-05, -2.6e-05, 5e-05, 1.2e-05, 7e-06, 4e-06, -4e-06, 0.0, 0.0, 0.0, -1e-06]
    # Assumption: Exposure-At-Default Values are generated randomly at the moment

    # Step 2: Simulate Step 0
    # failed(banks, eadValues, 0);
    generateExposures()
    getEAD()
    # Step 3: Simulate Step 1
    # failed(banks, eadValues, 1);
    # Step 5: Simulate Step q > 1

#Calculate the number of failed banks
def failed(banks, SeadMatrix, step):
    if (step == 0):
        pi = np.pi
        tested = np.power(pi, SeadMatrix)
        for bank in tested:
            if (bank >= 1):
                i, = np.where(tested == bank)
                failedSet.add(i[0]+1)
        # print(failedSet)
    # elif (step > 0):
    #     for bank in banks:
    #         if (bank not in failedSet):
    #             i = bank-1
    #             for bank in failedSet:
    #                 j = bank


    print(failedSet)

def getRand(range0, range1):
    return rand.uniform(range0, range1);


# banks = dict()
def generateExposures():
    for i in range(0, 22):
    # use 0 as starting point to avoid index out of range for the bankList array
    # for i in range(1, 23):

        B = Bank()
        bankList.append(B)
        # banks[i] = dict();
        # banks[i]["fixed_income_exposure"] = getRand(0.35,0.6)*(10**9);
        # banks[i]["derivatives_exposure"] = getRand(0, 0.3)*(10**9);
        # banks[i]["securities_financing_exposure"] = getRand(0.65, 0.9)*(10**9);
        # banks[i]["sum_exposures"] = banks[i]["derivatives_exposure"]+banks[i]["fixed_income_exposure"]+banks[i]["securities_financing_exposure"]
        # ten_pc_exp = 0.1*banks[i]["sum_exposures"]
        # fifteen_pc_exp = 0.15*banks[i]["sum_exposures"]
        # banks[i]["min_cap"] = getRand(ten_pc_exp, fifteen_pc_exp)
        # (Update: The above code are moved into the Object Bank's constructor )
        randfit = False

        '''
        IGNORE THIS CHUNK OF CODE - USED FOR TESTING IDEAS ONLY

        # randCap = getRand(0.0,0.1)*(10**11)
        # fifteen_pc_ac = 0.15*randCap
        # sixty_five_pc_ac = 0.65*randCap
        # a_cap = randCap - B.min_cap
        # print "rancap " + str(randCap)
        # print "mincap "+ str(B.min_cap)
        # print "fifmac "+ str(fifteen_pc_ac)
        # print "sixmac "+ str(sixty_five_pc_ac)
        # if (( fifteen_pc_ac < a_cap) and (a_cap < sixty_five_pc_ac)):
        #     print "fits"
        #     sixty_five_pc_ac = 0.65*randCa
        '''

        while (randfit == False):
            randCap = getRand(0.0,0.1)*(10**11)
            # print "mincap "+ str(B.min_cap)
            # print "rancap " + str(randCap)
            # print "========="
            # a_cap = randCap-banks[i]["min_cap"]
            a_cap = randCap - bankList[i].min_cap
            fifteen_pc_ac = 0.15*randCap
            sixty_five_pc_ac = 0.65*randCap
            if (( fifteen_pc_ac < a_cap) and (a_cap < sixty_five_pc_ac)):
                # banks[i]["capital"] = randCap;
                bankList[i].capital = randCap;
                # banks[i]["available_capital"] = a_cap;
                bankList[i].available_capital = a_cap
                randfit = True
                # print banks[i]["capital"]
            else:
                print "else triggered"
                randCap = getRand(0.3,0.45)*(10**9)
                fifteen_pc_ac = 0.65*randCap
                sixty_fix_pc_ac = 0.65*randCap
    # for j in range(0,22):
    #     print bankList[j]

def getEAD():
    eadMat = [];
    for bank in bankList:
        eadMat.append(bank.derivatives_exposure)
    print eadMat
    return eadMat

# def runcontagionsteps(n):
    # if (n == 0):


if __name__ == "__main__":
    main()
