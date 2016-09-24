import random as r
import numpy as np

f = lambda inputs : np.dot(inputs + [1], [88, 915, 10])

trainings = [[r.randint(0,100), r.randint(0,100)] for x in range(100)]
tests = [[r.randint(0,100), r.randint(0,100)] for x in range(100)]

set_training = [{
    'inputs' :  t,
    'output' :  f(t)
} for t in trainings]

set_test = [{
    'inputs' :  t,
    'output' : f(t)
} for t in tests]
