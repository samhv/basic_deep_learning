import numpy as np
from neuron import Neuron
from network import Network

class Test:
    def __init__(self, network):
        network.set_your_result_to(self)
        self.results = []
        self.network = network
        self.run()
    def set_result(self, network, outputs):
        t = self.current_test['output']
        y = [0 for o in outputs]
        for index in outputs:
            o = outputs[index]
            y[o['index']] = o['value']
        error = 0.5*sum([x**2 for x in np.subtract(y, t)])
        self.results.append(error)
    def summary(self):
        avg = np.sum(self.results)/len(self.results)
        print "error: %s" % (avg)
    def do_tests(self, set_test):
        self.results = []
        for test in set_test:
            self.current_test = test
            self.network.forward(test['inputs'])
            self.network.reset()
        self.summary()
    def run(self):
        from sets import set_training
        from sets import set_test
        self.do_tests(set_test)
        self.network.training(set_training)
        self.do_tests(set_test)
