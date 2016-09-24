import numpy as np

class Neuron:
    def __init__(self, weights, bias, function, rate):
        self.weights = weights + [bias]
        self.function = function
        self.rate = rate
    def forward(self, inputs):
        z = np.dot(inputs + [1], self.weights)
        y = self.function(z)
        return y
    def training(self, set_training):
        for training in set_training:
            t = training['output']
            y = self.forward(training['inputs'])
            inputs = training['inputs'] + [1]
            for i in range(len(self.weights)):
                delta = self.rate * inputs[i] * (t - y)
                self.weights[i] = self.weights[i] + delta
