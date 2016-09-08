# import matplotlib.pyplot as plt
import numpy as np
import sys
import math

# Ugly code for thinking about linear regression with gradient descent

################################################################
### Load the dataset
class linreg:

    def __init__(self):
        self.DOJIA = []
        self.temp = []
        self.avgtemp =[]
        self.tweight = np.random.rand(1)
        self.tbias = np.random.rand(1)
        self.dweight = np.random.rand(1)
        self.dbias = np.random.rand(1)
        self.difftemp = []

    def read(self, filename, dependent):
        my_data = np.genfromtxt(filename, delimiter=';', skip_header=1)
        self.DOJIA = my_data[:, dependent]
        self.temp = my_data[:, 2]
        self.avgtemp = my_data[:,3]
        self.difftemp = self.temp-self.avgtemp


################################################################
### Init the model parameters
    def templinregression(self):

        learning_rate = 0.007
        init_cost = 0
        end_cost = 0
        for i in range(len(self.temp)):
            error = (self.temp[i]*self.tweight+self.tbias)-self.DOJIA[i]
            self.tweight = self.tweight - learning_rate * error * self.temp[i]/len(self.temp)
            self.tbias = self.tbias - learning_rate*error*1.0/len(self.temp)
            init_cost += math.pow(error,2)
            new_error = (self.temp[i]*self.tweight+self.tbias)-self.DOJIA[i]
            end_cost += math.pow(new_error,2)
        print init_cost, end_cost
        return end_cost

    def difflinregression(self):
        learning_rate = 0.05
        init_cost = 0
        end_cost = 0
        for i in range(len(self.difftemp)):
            error = self.difftemp[i]*self.dweight+self.dbias-self.DOJIA[i]
            self.dweight = self.dweight - learning_rate * error * self.difftemp[i]/len(self.difftemp)
            self.dbias = self.dbias - learning_rate*error*1.0/len(self.difftemp)
            error = math.pow(error, 2)
            init_cost += error
            new_error = (self.difftemp[i]*self.dweight+self.dbias)-self.DOJIA[i]
            new_error = math.pow(new_error,2)
            end_cost += new_error
        print init_cost, end_cost
        return end_cost

    def getDiffWeights(self):
        print self.dweight, self.dbias

    def getTempWeights(self):
        print self.tweight, self.tbias

if __name__ == '__main__':
    np.random.seed(42) # Get the same random numbers every time
    model = linreg()
    model.read(sys.argv[1], sys.argv[2])
    print "Only temp"
    testval = model.templinregression()
    oldtest_val = 0
    while np.absolute(testval-oldtest_val) > 1:
        oldtest_val = testval
        testval = model.templinregression()
    print "\nDifference between temp and highest average temp"
    value = model.difflinregression()
    old_val = 0
    while np.absolute(value - old_val) > 1:
        old_val = value
        value = model.difflinregression()
    print "Theta for difference in temp and highest avg temp:"
    model.getDiffWeights()
    print "Theta for temperature"
    model.getTempWeights()

################################################################
### Graph the dataset along with the line defined by the model
#
# xs = np.arange(0, 5)
# ys = xs * tbias + bias
#
# plt.plot(hs_gpa, col_gpa, 'r+', xs, ys, 'g-')
# plt.show()
