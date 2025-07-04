import numpy as np
inputs = [[1.3,2.2,1.1,2.9],
          [0.3,1.2,2.1,0.9],
          [2.3,0.2,0.1,1.9],
          [-1.3,2.2,2.1,3.9]]
# let's say 3 neurons in layer1 and 3 in layer2
weights1 = [[1.3,0.5,-0.2,2.2],
           [-1,-1.5,-1.2,2],
           [-1.2,-2.5,-2.2,1.2]]
# layer2 weights
weights2 = [[2.3,0.5,0.2,1.2],
           [-2,-1.2,1.2,2],
           [-3.2,-2.5,-1.2,0.2]]
# single bias value for each neuron
biases1 = [2,3,1]
biases2 = [1,2,4,3]

# neurons performs the operations by the dot product(numpy)

# layer 1 output
layer1_output = np.dot(inputs,np.array(weights1).T)+biases1
# layer 2 output
layer2_output = np.dot(layer1_output,np.array(weights2))+biases2

print(layer2_output)
