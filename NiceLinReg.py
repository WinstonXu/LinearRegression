
import numpy as np
import sys
import math
from ReadData import ReadData

class NiceLinReg:

    def __init__(self):
        self.weight = np.random.rand(1)
        self.bias  = np.random.rand(1)

    def linreg(self, learning_rate, ind, dep):
        init_cost = np.sum(np.power((ind*self.weight+self.bias) - dep, 2))
        error = (ind*self.weight+self.bias) - dep
        self.weight = self.weight - np.sum(learning_rate * error * dep/ len(ind))
        self.bias = self.bias - np.sum(learning_rate * error * 1.0 / len(ind))
        end_cost = np.sum(np.power((ind*self.weight+self.bias) - dep, 2))
        print init_cost, end_cost
        return end_cost

    def train(self, learning_rate, ind, dep):
        val = self.linreg(learning_rate, ind, dep)
        old_val = 0
        #Can change this variable to decide how much convergence is wanted
        while np.absolute(val-old_val) > 1:
            old_val = val
            val = self.linreg(learning_rate, ind, dep)
        self.getTheta()

    def getTheta(self):
        print "Weight     Bias"
        print self.weight, self.bias

if __name__ == '__main__':
    #command line to run this properly
    #python NiceLinReg.py data.csv [2,3] 1
    np.random.seed(42)
    loader = ReadData()
    loader.load(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    print "Temp Only"
    tempOnly = NiceLinReg()
    dailyTemp = loader.getInd(0)
    DOJIA = loader.getDep()
    tempOnly.train(.000005, dailyTemp, DOJIA)

    print "\nDiff in Temp and avg highest recorded temp"
    diff = NiceLinReg()
    diffList = loader.diff(0,1)
    diff.train(0.000000000049, diffList, DOJIA)
