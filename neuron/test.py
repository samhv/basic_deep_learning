import numpy as np
from neuron import Neuron
from sets import set_training, set_test

def summary(neuron, set_test):
    w = neuron.weights
    t = [x['output'] for x in set_test]
    y = [neuron.forward(x['inputs']) for x in set_test]
    error = 0.5*sum([x**2 for x in np.subtract(y, t)])
    print "w=%s\ny=%s\nt=%s\ne=%s\n" % (w, y, t, error)
    return error

weights = [0,0]
bias = 0
function = lambda z : z
rate = 1.0/10000

neuron = Neuron(weights, bias, function, rate)

e1 = summary(neuron, set_test)
neuron.training(set_training)
e2 = summary(neuron, set_test)

print "fallo=%s\n" % (e2/e1)
