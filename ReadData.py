
import numpy as np

class ReadData:

    def __init__(self):
        self.independent = []
        self.dependent = []

    def load(self, filename, ind, dep):
        my_data = np.genfromtxt(filename, delimiter=';', skip_header=1)
        self.dependent = my_data[:,dep]
        indep = ind[1:len(ind)-1].split(',')
        for i in range(len(indep)):
            indep[i] = int(indep[i])
        self.independent = my_data[:,indep]

    def diff(self, col_1, col_2):
        diffList = np.power(self.independent[:, col_1]-self.independent[:,col_2],2)
        return diffList

    def getDep(self):
        return self.dependent

    def getInd(self, colNum):
        return self.independent[:, colNum]
