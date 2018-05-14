import math
from tabulate import tabulate
class geElec:
    def __init__(forwardDiff, X, fOfX, fConstant):
        forwardDiff.X = X
        forwardDiff.fOfX = fOfX
        forwardDiff.fConstant = fConstant

    def calculate(forwardDiff):
        forwardDiff.X = forwardDiff.X.split(',')
        forwardDiff.fOfX = forwardDiff.fOfX.split(',')
        forwardDiff.fConstant = float(forwardDiff.fConstant)
        xList = []
        delta = []
        first = []
        ans = []
        for i in forwardDiff.X:
            i = float(i)
            xList.append(i)
        for j in forwardDiff.fOfX:
            j = float(j)
            delta.append(j)
        h = xList[1] - xList[0]  # interval
        r = (forwardDiff.fConstant - xList[0]) / h

        obj = {}
        for k in range(0, len(xList)-1):
            obj["delta" + str(k)] = []
            for m in range(0, len(delta)-1):
                m = delta[m+1] - delta[m]
                m = obj["delta" + str(k)].append(m)
            delta = obj["delta" + str(k)]
            first.append(delta[0])
        for c in range(0, len(first)):
            if c == 0:
                c = delta[0]
                ans.append(c)
            if c == 1:
                c = r * first[c - 1]
                ans.append(c)
            if c == 2:
                c = r * (r - 1) * (first[c - 1] / math.factorial(c))
                ans.append(c)
            if c == 3:
                c = r * (r - 1) * (r - 2) * (first[c - 1] / math.factorial(c))
                ans.append(c)
            if c == 4:
                c = r * (r - 1) * (r - 2) * (r - 3) * (first[c - 1] / math.factorial(c))
                ans.append(c)
        b = sum(ans)
        print(tabulate(obj, headers=["X", "f(X)", "delta1", "delta2", "delta3", "delta4", "delta5"], tablefmt='orgtbl'))
        print("\nf(" + str(forwardDiff.fConstant) + ") = " + str(b))

inpX = input("Input X: ")
inpFoX = input("Input f(X): ")
inpFCons = input("Input value of X: ")
out = geElec(inpX, inpFoX, inpFCons)
out.calculate()
