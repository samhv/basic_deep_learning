class Network:
    def __init__(self, input_neurons, output_neurons):
        self.output_neurons = output_neurons
        self.running = False
        self.input_neurons = input_neurons
        self.dimension = len(output_neurons)
        self.count_outputs = 0
        self.outputs = {}
        self.to_send_result = None
        for index in range(self.dimension):
            neuron = output_neurons[index]
            self.outputs[neuron] = {
                'index' : index
            }
            neuron.set_your_output_to(self)
    def forward(self, inputs):
        self.running = True
        for neuron in self.input_neurons:
            for i in inputs:
                neuron.set_input(self, i)
    def set_your_result_to(self, someone):
        self.to_send_result = someone
    def set_input(self, neuron, value):
        self.outputs[neuron] = {
            'index' : self.outputs[neuron]['index'],
            'value' : value
        }
        self.count_outputs += 1
        if self.count_outputs == self.dimension:
            self.to_send_result.set_result(self, self.outputs)
    def reset(self):
        if self.running:
            self.count_outputs = 0
            self.running = False
            for neuron in self.input_neurons:
                neuron.reset()
    def training(self, set_training):
        for training in set_training:
            t = training['output'] #[t1,t2,t3]
            self.forward(training['inputs'])
            for neuron in self.output_neurons:
                real_value = t[self.outputs[neuron]['index']]
                neuron.update_your_weights(real_value)
            self.reset()
