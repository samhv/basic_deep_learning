from test import Test
from neuron import Neuron
from network import Network

x_1_1 = Neuron(3)
x_1_2 = Neuron(3)
x_1_3 = Neuron(3)
x_2_1 = Neuron([x_1_1, x_1_2, x_1_3])
x_2_2 = Neuron([x_1_1, x_1_2, x_1_3])
x_3 = Neuron([x_2_1, x_2_2])
x_4 = Neuron([x_3])
x_5_1 = Neuron([x_4])
x_5_2 = Neuron([x_4])
x_6_1 = Neuron([x_5_1])
x_6_2 = Neuron([x_5_2])
inputs = [x_1_1, x_1_2, x_1_3]
outputs = [x_6_1, x_6_2]
network = Network(inputs, outputs)
test = Test(network)
