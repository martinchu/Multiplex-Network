import random

precision = 1000000

def f(n) :
    matrix = []
    for l in range(n) :
        lineLst = []
        sum = 0
        crtPrec = precision
        for i in range(n-1) :
            val = random.randrange(crtPrec)
            sum += val
            lineLst.append(float(val)/precision)
            crtPrec -= val
        lineLst.append(float(precision - sum)/precision)
        matrix.append(lineLst)
    return matrix


matrix = f(22)
print matrix