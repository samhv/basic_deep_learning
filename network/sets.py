import math as m
import random as r
import numpy as np

f = lambda x : [x[0]*x[1], x[1]*x[2]/x[0] ]

trainings = [[r.randint(1,100), r.randint(1,100), r.randint(1,100)] for x in range(100000)]
tests = [[r.randint(1,100), r.randint(1,100), r.randint(1,100)] for x in range(100000)]

set_training = [{
    'inputs' :  t,
    'output' :  f(t)
} for t in trainings]

set_test = [{
    'inputs' :  t,
    'output' : f(t)
} for t in tests]
