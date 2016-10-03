import numpy as np

class Neuron:
    def __init__(self, input_neurons):
        self.input_neurons = input_neurons
        if isinstance(input_neurons,int):
            self.input_dimension = input_neurons + 1 #bases
        else:
            self.input_dimension = len(input_neurons) + 1
            for neuron in input_neurons:
                neuron.set_your_output_to(self)
        self.neurons_to_send_outputs = []
        self.inputs = []
        self.weights = [1 for x in range(self.input_dimension)]
        self.function = lambda x : x
        self.rate = 1.0/10000000
        self.hope_value = 0
    def forward(self, inputs):
        z = np.dot(inputs + [1], self.weights)
        y = self.function(z)
        self.hope_value = y
        for neuron in self.neurons_to_send_outputs:
            neuron.set_input(self, y)
    def reset(self):
        self.inputs = []
        for neuron in self.neurons_to_send_outputs:
            neuron.reset()
    def set_input(self, neuron, value):
        self.inputs.append({
            'neuron' : neuron,
            'value' : value
        })
        if (len(self.inputs)+1) == self.input_dimension:
            self.forward([x['value'] for x in self.inputs])
    def set_your_output_to(self, neuron):
        self.neurons_to_send_outputs.append(neuron)
    def update_your_weights(self, real_value):
        y = self.hope_value
        t = real_value
        inputs = [x['value'] for x in self.inputs] + [1]
        new_values = {}
        for i in range(len(self.weights)):
            delta_weights = self.rate * inputs[i] * (t - y)
            self.weights[i] = self.weights[i] + delta_weights
            delta_input = 0
        if not isinstance(self.input_neurons, int):
            for i in range(len(self.input_neurons)):
                if self.weights[i] != 0:
                    for j in range(len(self.weights)):
                        if j != i:
                            delta_input += self.weights[j]*inputs[j]
                    new_values[self.input_neurons[i]] = (t - delta_input)/self.weights[i]
                else:
                    new_values[self.input_neurons[i]] = y + self.rate*(t-y)
            for neuron in self.input_neurons:
                neuron.update_your_weights(new_values[neuron])
